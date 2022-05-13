import os
import spack.cmd
import logging
import shutil
import llnl.util.tty as tty
import spack.util.spack_yaml as syaml
from spack.extensions.stack.env import StackEnv

logging.basicConfig(level=logging.INFO)

description = "Create spack-stack environment"
section = "spack-stack-env"
level = "long"

subcommands = [
    'create',
]


def spack_stack_path():
    spack_stack_path = os.path.dirname(spack.paths.spack_root)
    dirname = os.path.basename(spack_stack_path)

    if dirname != 'spack-stack':
        raise Exception('Not a submodule of spack-stack')

    return spack_stack_path


default_env_name = 'default'
default_env_path = os.path.join(spack_stack_path(), 'envs')


def stack_create_setup_parser(subparser):
    subparser.add_argument(
        '--name', type=str, required=False, default=default_env_name,
        help='Environment name, defaults to {}.'.format(default_env_name)
        'Environment will be in <prefix>/<name>'
    )

    subparser.add_argument(
        '--dir', type=str, required=False, default=default_env_path,
        help='Environment will be placed in <dir>/<name>.'
        'Default is {}.'.format(default_env_path)
    )

    subparser.add_argument(
        '--app', type=str, required=False, dest='app', default=None,
        help='App name in env_bundles_dict or a spack.yaml'
    )

    subparser.add_argument(
        '--site', type=str, required=False, default=None,
        help='Pre-configured platform to build for (e.g. hera, jet, orion)'
        'otherwise no machine-specific config files are included'
    )

    subparser.add_argument(
        '--envs-file', type=str, required=False, default=None,
        help='Create environments from envs.yaml file.'
        'Other command-line options will be ignored'
    )

    subparser.add_argument(
        '--overwrite', action='store_true', required=False, default=False,
        help='Overwrite existing environment, if it exists.'
        'Warning this is dangerous.'
    )


def stack_create(args):
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

    env_dir = os.path.join(dir, name)
    if os.path.exists(env_dir):
        if overwrite:
            tty.msg('Env {} exists. Overwriting...'.format(env_dir))
            shutil.rmtree(env_dir)

    if envs_file:
        logging.info('Creating envs from envs_file')
        with open(envs_file, 'r') as f:
            site_envs = syaml.load_config(stream=f)

        envs = site_envs['envs']
        for env in envs:
            stack_env = StackEnv(**env['env'])
            stack_env.write()
    else:
        logging.info('Creating envs from command-line args')
        stack_env = StackEnv(name=name, dir=dir, site=site, app=app)
        stack_env.write()


#: Dictionary mapping subcommand names and aliases to functions
subcommand_functions = {}


def setup_parser(subparser):
    sp = subparser.add_subparsers(metavar='SUBCOMMAND', dest='stack_command')

    for name in subcommands:
        if isinstance(name, (list, tuple)):
            name, aliases = name[0], name[1:]
        else:
            aliases = []

        # add commands to subcommands dict
        function_name = 'stack_%s' % name
        function = globals()[function_name]
        for alias in [name] + aliases:
            subcommand_functions[alias] = function

        # make a subparser and run the command's setup function on it
        setup_parser_cmd_name = 'stack_%s_setup_parser' % name
        setup_parser_cmd = globals()[setup_parser_cmd_name]

        subsubparser = sp.add_parser(
            name, aliases=aliases, help=setup_parser_cmd.__doc__)
        setup_parser_cmd(subsubparser)


# Main command that calls subcommands
def stack(parser, args):
    """Look for a function called environment_<name> and call it."""
    action = subcommand_functions[args.stack_command]
    action(args)
