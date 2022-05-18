import spack.cmd.common.arguments
import spack.cmd.modules
import os
import logging
from spack.extensions.stack.env import StackEnv, stack_path
import shutil
import llnl.util.tty as tty
import spack.util.spack_yaml as syaml

description = "Create spack-stack environment"
section = "spack-stack-env"
level = "long"

subcommands = [
    'create',
]


default_env_name = 'default'
default_env_path = os.path.join(stack_path(), 'envs')
default_packages = os.path.join(stack_path(),
                                'configs', 'common', 'packages.yaml')
stack_app_path = os.path.join(stack_path(), 'configs', 'apps')


def setup_create_parser(subparser):
    subparser.add_argument(
        '--name', type=str, required=False, default=default_env_name,
        help='Environment name, defaults to {}.'.format(default_env_name) +
        ' Environment will be in <prefix>/<name>'
    )

    subparser.add_argument(
        '--dir', type=str, required=False, default=default_env_path,
        help='Environment will be placed in <dir>/<name>.'
        ' Default is {}.'.format(default_env_path)
    )

    subparser.add_argument(
        '--app', type=str, required=False, dest='app', default=None,
        help='Either a named app in (configs/apps) or path to spack.yaml'
        ' to be used as the base for further customization.'
    )

    subparser.add_argument(
        '--site', type=str, required=False, default='default',
        help='Pre-configured platform to build for (e.g. hera, jet, orion)'
        ' otherwise no machine-specific config files are included'
    )

    subparser.add_argument(
        '--container', type=str, required=False, default=None,
        help='Container template. Create a container based on an app\'s'
        ' packages and specs.'
    )

    subparser.add_argument(
        '--envs-file', type=str, required=False, default=None,
        help='Create environments from envs.yaml file.'
        ' Other command-line options will be ignored'
    )

    subparser.add_argument(
        '--overwrite', action='store_true', required=False, default=False,
        help='Overwrite existing environment, if it exists.'
        ' Warning this is dangerous.'
    )

    subparser.add_argument(
        '--base-packages', type=str, required=False, default=default_packages,
        help='Base packages.yaml.'
        ' Defaults to {}'.format(default_packages)
    )

    subparser.add_argument(
        '--prefix', type=str, required=False, default=None,
        help='Install prefix.'
    )

    subparser.add_argument(
        '--module-prefix', type=str, required=False, default='modulefiles',
        help='Module install prefix. Modules will be placed relative to'
             'install prefix or absolute path if given.'
    )

    subparser.add_argument(
        '--no-common', action='store_true',
        help='Do not use common config files.'
    )

    subparser.add_argument(
        '--no-includes', action='store_true', required=False, default=None,
        help='Copy base-packges directly into spack.yaml (no includes)'
        ' Useful in containers that cannot have includes.'
        ' Warning this will break with packages that have "::" because'
        ' of a bug with Spack the replaces it with a quote when used in'
        ' a spack.yaml.'
    )


def setup_env_parser(subparser):
    sp = subparser.add_subparsers(metavar='SUBCOMMAND', dest='env_command')
    create_parser = sp.add_parser('create',
                                  help='Create local Spack environmnent')
    setup_create_parser(create_parser)


def env_create(args):
    """Create pre-configured Spack environment.

    Args: args

    Returns:

    """
    site = args.site
    app = args.app
    name = args.name
    dir = args.dir
    envs_file = args.envs_file
    overwrite = args.overwrite
    install_prefix = args.prefix
    module_prefix = args.module_prefix
    no_common = args.no_common
    container = args.container

    base_packages = args.base_packages
    no_includes = args.no_includes

    env_dir = os.path.join(dir, name)
    if os.path.exists(env_dir):
        if overwrite:
            tty.msg('Env {} exists. Overwriting...'.format(env_dir))
            shutil.rmtree(env_dir)

    if envs_file:
        logging.debug('Creating envs from envs_file')
        with open(envs_file, 'r') as f:
            site_envs = syaml.load_config(stream=f)

        envs = site_envs['envs']
        for env in envs:
            stack_env = StackEnv(**env['env'])
            stack_env.write()
    else:
        logging.debug('Creating envs from command-line args')
        stack_env = StackEnv(name=name, dir=dir, site=site, app=app,
                             base_packages=base_packages,
                             no_includes=no_includes,
                             install_prefix=install_prefix,
                             module_prefix=module_prefix,
                             no_common=no_common
                             )
        stack_env.write()
