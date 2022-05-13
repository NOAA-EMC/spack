import spack
import os
import logging
import spack.util.spack_yaml as syaml

default_manifest_yaml = """\
# This is a Spack Environment file.
#
# It describes a set of packages to be installed, along with
# configuration settings.
spack:

  view: false

"""

app_specs = {
    'jedi-all': ['jedi-fv3-bundle-env', 'jedi-ufs-bundle-env', 'jedi-um-bundle-env', 'soca-bundle-env'],
    'jedi-fv3': ['jedi-fv3-bundle-env'],
    'jedi-tools': ['jedi-tools-env'],
    'jedi-ufs': ['jedi-ufs-bundle-env'],
    'jedi-ufs-all': ['jedi-ufs-all-env', 'ufs-weather-model-debug-env'],
    'jedi-um': ['jedi-um-bundle-env'],
    'nceplibs-bundle-env': ['nceplibs-bundle-env'],
    'soca': ['soca-bundle-env'],
    'ufs-weather-model': ['ufs-weather-model-env', 'ufs-weather-model-debug-env'],
    'test': ['zlib'],
}



class StackEnv():
    """ Represents a spack.yaml environment based on different
    configurations of sites and specs. Construct with an envs.yaml or
    through the command line. Uses Spack's library
    to maintain an internal state that represents the yaml and can be
    written out with write().
    Construct with an envs.yaml or through the command line.
    The output is a pure Spack environment which can be used as normal.
    """
    def __init__(self, **kwargs):
        """
        Construct properties directly from kwargs so they can be passed in
        through a dictionary (input file), or named args
        for command-line usage.
        """

        self.includes = []
        self.specs = []
        self.env_yaml = syaml.load_config(default_manifest_yaml)

        self.name = kwargs.get('name')
        self.dir = kwargs.get('dir')

        self.app = kwargs.get('app', None)
        if self.app:
            self.add_specs(app_specs[self.app])

        self.site = kwargs.get('site', None)
        self.desc = kwargs.get('desc', None)
        self.compiler = kwargs.get('compiler', None)
        self.mpi = kwargs.get('mpi', None)
        self.intsall_prefix = kwargs.get('install_prefix', None)

    def env_dir(self):
        """env_dir is <dir>/<name>"""
        return os.path.join(self.dir, self.name)

    def add_specs(self, specs):
        self.specs.extend(specs)

    def add_includes(self, includes):
        self.includes.extend(includes)

    def add_config(self, path):
        """Add config path to spack.yaml.
        For example: "packages:all:compiler:value"
        """
        root = self.env_yaml['spack']
        components = path.split(':')

        value = components.pop()
        current_path = ''
        for idx, comp in enumerate(components):
            # Create new path from here on
            if comp not in root:
                for i, component in enumerate(components[idx:]):

                    if (i+1) == len(components[idx:]):
                        root[component] = value
                    else:
                        root[component] = {}

                    root = root[component]
                break

            root = root[comp]

    def _copy_site_includes(self):
        if not self.site:
            raise Exception('Site is not set')

        self.includes.append('site')
        site_configs_dir = os.path.join(site_path, self.site)
        env_site_dir = os.path.join(self.env_dir, 'site')
        shutil.copytree(site_configs_dir, env_site_dir)

    def write(self):
        """Write environment out to a spack.yaml in <env_dir>/<name>.
        Will create env_dir if it does not exist.
        """
        env_dir = self.env_dir()
        env_yaml = self.env_yaml

        if os.path.exists(env_dir):
            raise Exception("Environment '{}' already exists.".format(env_dir))

        if self.site:
            self._copy_site_includes

        os.makedirs(env_dir, exist_ok=True)

        if self.compiler:
            self.add_config('packages:all:compiler:[{}]'.format(self.compiler))

        if self.mpi:
            self.add_config('packages:all:providers:mpi:[{}]'.format(self.mpi))

        env_yaml['spack']['include'] = self.includes

        env_yaml['spack']['specs'] = self.specs

        env_file = os.path.join(env_dir, 'spack.yaml')
        with open(env_file, 'w') as f:
            syaml.dump_config(env_yaml, stream=f)

        logging.info('Successfully wrote environment at {}'.format(env_file))
