import pytest
import spack.main
import os
import spack

stack_create = spack.main.SpackCommand('stack')


# Find spack-stack directory assuming this Spack instance
# is a submodule of spack-stack.
def stack_path(*paths):
    stack_dir = os.path.dirname(spack.paths.spack_root)

    if not os.path.exists(os.path.join(stack_dir, '.spackstack')):
        raise Exception('Not a submodule of spack-stack')

    return os.path.join(stack_dir, *paths)


test_dir = stack_path('envs', 'unit-tests')


def all_apps():
    _, apps, _ = next(os.walk(stack_path('configs', 'apps')))
    return list(apps)


def all_sites():
    _, sites, _ = next(os.walk(stack_path('configs', 'sites')))
    return list(sites)


def all_containers():
    _, _, containers = next(os.walk(stack_path('configs', 'containers')))
    return containers

def all_specs():
    bundles_dir = os.path.join(spack.paths.var_path, 'repos', 'jcsda-emc-bundles', 'packages')
    _, bundle_envs, _ = next(os.walk(bundles_dir))
    return bundle_envs


@pytest.mark.extension('stack')
@pytest.mark.parametrize('app', all_apps())
@pytest.mark.filterwarnings('ignore::UserWarning')
def test_apps(app):
    output = stack_create('create', 'environment', '--app', app,
                          '--dir', test_dir, '--overwrite')


@pytest.mark.extension('stack')
@pytest.mark.parametrize('site', all_sites())
@pytest.mark.filterwarnings('ignore::UserWarning')
def test_sites(site):
    output = stack_create('create', 'environment', '--site', site,
                          '--dir', test_dir, '--overwrite')


@pytest.mark.extension('stack')
@pytest.mark.parametrize('container', all_containers())
@pytest.mark.filterwarnings('ignore::UserWarning')
def test_containers(container):
    container_wo_ext = os.path.splitext(container)[0]
    output = stack_create('create', 'container', container_wo_ext, '--app', 'empty',
                          '--dir', test_dir, '--overwrite')


@pytest.mark.extension('stack')
@pytest.mark.parametrize('spec', all_specs())
@pytest.mark.filterwarnings('ignore::UserWarning')
def test_containers(spec):
    output = stack_create('create', 'environment', '--specs', spec,
                          '--dir', test_dir, '--overwrite')
