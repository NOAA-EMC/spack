import os

import spack

# Hidden file in top-level spack-stack dir so this module can
# find relative config files. Assuming Spack is a submodule of
# spack-stack.
check_file = '.spackstack'
stack_dir = os.path.dirname(spack.paths.spack_root)


def is_stack_submodule():
    return os.path.exists(os.path.join(stack_dir, check_file))


def stack_path(*paths):
    stack_dir = os.path.dirname(spack.paths.spack_root)

    if not is_stack_submodule():
        print("Not a submodule of spack-stack, exiting")
        exit(0)

    return os.path.join(stack_dir, *paths)


common_path = stack_path('configs', 'common')
site_path = stack_path('configs', 'sites')
container_path = stack_path('configs', 'containers')
template_path = stack_path('configs', 'templates')
default_env_path = stack_path('envs')
