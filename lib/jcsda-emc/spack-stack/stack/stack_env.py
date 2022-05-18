import subprocess
from platformdirs import site_config_dir
import spack
import os
import logging
import spack.util.spack_yaml as syaml
import spack.environment as ev
import shutil
import llnl.util.tty as tty
import spack.config

default_manifest_yaml = """\
# This is a Spack Environment file.
#
# It describes a set of packages to be installed, along with
# configuration settings.
# Includes are in order of highest precedence first.
# Site configs take precedence over the base packages.yaml.
spack:

  view: false

"""

valid_configs = ['compilers.yaml', 'config.yaml', 'mirrors.yaml',
                 'modules.yaml', 'packages.yaml', 'concretizer.yaml']

# Hidden file in top-level spack-stack dir so this module can
# find relative config files. Assuming Spack is a submodule of
# spack-stack.
check_file = '.spackstack'


# Find spack-stack directory assuming this Spack instance
# is a submodule of spack-stack.
def stack_path():
    stack_path = os.path.dirname(spack.paths.spack_root)

    if not os.path.exists(os.path.join(stack_path, check_file)):
        raise Exception('Not a submodule of spack-stack')

    return stack_path


site_path = os.path.join(stack_path(), 'configs', 'sites')
app_path = os.path.join(stack_path(), 'configs', 'apps')

# Use SPACK_STACK_DIR for these configs because changes in these
# files should be tracked as part of the repo.
common_includes = ['${SPACK_STACK_DIR}/configs/common/modules.yaml',
                   '${SPACK_STACK_DIR}/configs/common/config.yaml']


def get_git_revision_short_hash(path) -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                   cwd=path).decode('ascii').strip()


def stack_hash():
    return get_git_revision_short_hash(stack_path())


def spack_hash():
    return get_git_revision_short_hash(spack.paths.spack_root)


class StackEnv(object):
    """ Represents a spack.yaml environment based on different
    configurations of sites and specs. Can be created through an envs.yaml or
    through the command line. Uses Spack's library
    to maintain an internal state that represents the yaml and can be
    written out with write().
    The output is a pure Spack environment.
    """

    def __init__(self, **kwargs):
        """
        Construct properties directly from kwargs so they can be passed in
        through a dictionary (input file), or named args
        for command-line usage.
        """

        self.name = kwargs.get('name')
        self.dir = kwargs.get('dir')

        self.specs = []
        self.includes = []

        self.app = kwargs.get('app', None)

        # Config can be either name in apps dir or an absolute path to
        # to a spack.yaml to be used as a template. If None then empty
        # template is used.

        if not self.app:
            self.env_yaml = syaml.load_config(default_manifest_yaml)
            self.app_path = None
        else:
            if os.path.isabs(self.app):
                self.app_path = self.app
                template = self.app
            elif os.path.exists(os.path.join(app_path, self.app)):
                self.app_path = os.path.join(app_path, self.app)
                template = os.path.join(app_path, self.app, 'spack.yaml')

            with open(template, 'r') as f:
                self.env_yaml = syaml.load_config(f)

        self.site = kwargs.get('site', None)
        self.desc = kwargs.get('desc', None)
        self.compiler = kwargs.get('compiler', None)
        self.mpi = kwargs.get('mpi', None)
        self.base_packages = kwargs.get('base_packages', None)
        self.no_includes = kwargs.get('no_includes', None)
        self.install_prefix = kwargs.get('install_prefix', None)
        self.module_prefix = kwargs.get('module_prefix', None)
        self.no_common = kwargs.get('no_common', None)
        self.mirror = kwargs.get('mirror', None)
        self.upstream = kwargs.get('upstreams', None)

    def env_dir(self):
        """env_dir is <dir>/<name>"""
        return os.path.join(self.dir, self.name)

    def add_specs(self, specs):
        self.specs.extend(specs)

    def add_includes(self, includes):
        self.includes.extend(includes)

    def site_configs_dir(self):
        site_configs_dir = os.path.join(site_path, self.site)
        return site_configs_dir

    def _copy_site_includes(self):
        """Copy site directory into environment"""
        if not self.site:
            raise Exception('Site is not set')

        site_name = 'site.{}'.format(self.site)
        self.includes.append(site_name)
        env_site_dir = os.path.join(self.env_dir(), site_name)
        shutil.copytree(self.site_configs_dir(), env_site_dir)

    def _copy_package_includes(self):
        """Copy base packages into environment"""
        if not self.base_packages:
            raise Exception('base_packages is not set')

        self.add_includes(['packages.yaml'])
        shutil.copy(self.base_packages, self.env_dir())

    def write(self):
        """Write environment out to a spack.yaml in <env_dir>/<name>.
        Will create env_dir if it does not exist.
        """
        env_dir = self.env_dir()
        env_yaml = self.env_yaml

        if os.path.exists(env_dir):
            raise Exception("Environment '{}' already exists.".format(env_dir))

        os.makedirs(env_dir, exist_ok=True)

        if not self.no_common:
            self.add_includes(common_includes)

        if not self.no_includes:
            if self.site:
                self._copy_site_includes()

            if self.base_packages:
                self._copy_package_includes()

        # No way to add to env includes using pure Spack.
        env_yaml['spack']['include'] = self.includes

        # Write out file with includes filled in.
        env_file = os.path.join(env_dir, 'spack.yaml')
        with open(env_file, 'w') as f:
            # Write header with hashes.
            header = 'spack-stack hash: {}\nspack hash: {}'
            env_yaml.yaml_set_start_comment(
                header.format(stack_hash(), spack_hash()))
            syaml.dump_config(env_yaml, stream=f)

        # Activate empty env and add specs/packages.
        env = ev.Environment(path=env_dir, init_file=env_file)
        ev.activate(env)
        env_scope = env.env_file_config_scope()
        env_scope_name = env.env_file_config_scope_name()

        # Save original data in spack.yaml because it has higest precedence.
        # spack.config.add will overwrite as it goes.
        # Precedence order (high to low) is original spack.yaml,
        # then common configs, then site configs.
        original_sections = {}
        for key in spack.config.section_schemas.keys():
            section = spack.config.get(key, scope=env_scope_name)
            if section:
                original_sections[key] = section

        # Copy config files directly into spack.yaml
        if self.no_includes:
            # Add basic packages.yaml
            if self.base_packages:
                spack.config.add_from_file(self.base_packages, env_scope_name)

            if self.site:
                for f in os.listdir(self.site_configs_dir()):
                    if f in valid_configs:
                        fullpath = os.path.join(self.site_configs_dir(), f)
                        spack.config.add_from_file(fullpath)

        # Commonly used config settings
        if self.compiler:
            compiler = 'packages:all::compiler:[{}]'.format(self.compiler)
            spack.config.add(compiler, scope=env_scope_name)
        if self.mpi:
            mpi = 'packages:all::providers:mpi:[{}]'.format(self.mpi)
            spack.config.add(mpi, scope=env_scope_name)
        if self.install_prefix:
            # Modules can go in <prefix>/modulefiles by default
            prefix = 'config:install_tree:root:{}'.format(self.install_prefix)
            spack.config.add(prefix, scope=env_scope_name)
            if not os.path.isabs(self.module_prefix):
                prefix = os.path.join(self.install_prefix,
                                      self.module_prefix)
            lmod_prefix = 'config:module_roots:lmod:{}'.format(prefix)
            tcl_prefix = 'config:module_roots:tcl:{}'.format(prefix)
            spack.config.add(lmod_prefix, scope=env_scope_name)
            spack.config.add(tcl_prefix, scope=env_scope_name)

        # Merge the original spack.yaml template back in
        # so it has the higest precedence
        for section in spack.config.section_schemas.keys():
            original = original_sections.get(section, {})
            existing = spack.config.get(section, scope=env_scope_name)
            existing = spack.config.merge_yaml(existing, original)
            if section in existing:
                spack.config.set(section, existing[section], env_scope_name)

        with env.write_transaction():
            specs = spack.cmd.parse_specs(self.specs)
            for spec in specs:
                env.add(spec)

            env.write()

        logging.info('Successfully wrote environment at {}'.format(env_file))
