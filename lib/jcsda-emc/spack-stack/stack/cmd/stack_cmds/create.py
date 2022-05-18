import spack.cmd.common.arguments
import spack.cmd.modules
import os
import logging
from spack.extensions.stack.stack_env import StackEnv, stack_path, app_path
from spack.extensions.stack.container_env import StackContainer
import shutil
import llnl.util.tty as tty
import spack.util.spack_yaml as syaml

description = "Create spack-stack environment (env or container)"
section = "spack-stack-env"
level = "long"

default_env_name = 'default'
default_env_path = os.path.join(stack_path(), 'envs')
default_packages = os.path.join(stack_path(),
                                'configs', 'common', 'packages.yaml')


def setup_container_parser(subparser):
    subparser.add_argument(
        'container', help='Container template to use in configs/containers')

    subparser.add_argument(
        '--app', type=str, required=True, dest='app', default=None,
        help='Either a named app in (configs/apps) or path to spack.yaml'
        ' to be used as the base for further customization.'
    )

    subparser.add_argument(
        '--name', type=str, required=False, default=None,
        help='Environment name, defaults to {}.'.format(default_env_name) +
        ' Environment will be in <prefix>/<name>'
    )

    subparser.add_argument(
        '--dir', type=str, required=False, default=default_env_path,
        help='Environment will be placed in <dir>/<name>/contents.'
        ' Default is {}.'.format(default_env_path)
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
        '--specs', type=str, required=False, default=default_packages,
        help='A specs.yaml or individual spec'
    )


def setup_env_parser(subparser):
    subparser.add_argument(
        '--name', type=str, required=False, default=default_env_name,
        help='Environment name, defaults to {}.'.format(default_env_name) +
        ' Environment will be in <prefix>/<name>'
    )

    subparser.add_argument(
        '--dir', type=str, required=False, default=default_env_path,
        help='Environment will be placed in <dir>/<name>/contents.'
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
        ' otherwise an empty site directory is created with default values.'
        ' Set to "none" for no site files at all.'
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


def setup_create_parser(subparser):
    sp = subparser.add_subparsers(metavar='SUBCOMMAND', dest='env_type')

    env_parser = sp.add_parser('env', help='Create local Spack environment')
    container_parser = sp.add_parser('container', help='Create container.')

    setup_env_parser(env_parser)

    setup_container_parser(container_parser)


def container_create(args):
    """Create pre-configured container"""

    container = StackContainer(args.container, args.app, args.name,
                               args.dir, args.base_packages)

    env_dir = container.env_dir
    if os.path.exists(env_dir):
        if args.overwrite:
            tty.msg('Env {} exists. Overwriting...'.format(env_dir))
            shutil.rmtree(env_dir)
        else:
            raise Exception('Env: {} already exists'.format(env_dir))

    container.write()
    tty.msg('Created container {}'.format(env_dir))


def dict_from_args(args):
    dict = {}
    dict['site'] = args.site
    dict['app'] = args.app
    dict['name'] = args.name
    dict['envs_file'] = args.envs_file
    dict['install_prefix'] = args.prefix
    dict['module_prefix'] = args.module_prefix
    dict['no_common'] = args.no_common
    dict['base_packages'] = args.base_packages
    dict['no_incldues'] = args.no_includes
    dict['dir'] = args.dir

    return dict


def env_create(args):
    """Create pre-configured Spack environment.

    Args: args

    Returns:

    """

    stack_settings = dict_from_args(args)
    stack_env = StackEnv(**stack_settings)

    env_dir = stack_env.env_dir()
    if os.path.exists(env_dir):
        if args.overwrite:
            tty.msg('Env {} exists. Overwriting...'.format(env_dir))
            shutil.rmtree(env_dir)
        else:
            raise Exception('Env: {} already exists'.format(env_dir))

    if args.envs_file:
        logging.debug('Creating envs from envs_file')
        with open(args.envs_file, 'r') as f:
            site_envs = syaml.load_config(stream=f)

        envs = site_envs['envs']
        for env in envs:
            stack_env = StackEnv(**env['env'])
            stack_env.write()
    else:
        logging.debug('Creating envs from command-line args')
        stack_env = StackEnv(**stack_settings)
        stack_env.write()


def stack_create(parser, args):
    if args.env_type == 'env':
        env_create(args)
    elif args.env_type == 'container':
        container_create(args)
