import os
import spack
import spack.util.spack_yaml as syaml
from spack.extensions.stack.stack_env import StackEnv, stack_path, app_path

container_path = os.path.join(stack_path(), 'configs', 'containers')


class StackContainer():
    """Represents an abstract container. It takes in a
    conatiner template (spack.yaml), the specs from an app, and
    its packages.yaml versions then writes out a merged file.
    """

    def __init__(self, container, app, name, dir, base_packages) -> None:
        if os.path.isabs(container):
            self.container_path = container
        elif os.path.exists(os.path.join(container_path, container)):
            self.container_path = os.path.join(container_path, container)
        else:
            raise Exception("Invalid container")

        if os.path.isabs(app):
            self.app_path = app
        elif os.path.exists(os.path.join(app_path, app)):
            self.app_path = os.path.join(app_path, app)
        else:
            raise Exception("Invalid app")

        basename = os.path.basename(self.container_path)
        self.name = name if name else '{}.{}'.format(basename, app)

        self.dir = dir
        self.env_dir = os.path.join(self.dir, self.name)
        self.base_packages = base_packages

    def write(self):
        """Merge base packages and app's spack.yaml into
        output container file
        """
        app_env = os.path.join(self.app_path, 'spack.yaml')
        sections = ['packages', 'specs']
        with open(app_env, 'r') as f:
            app_yaml = syaml.load_config(f)

        with open(self.container_path, 'r') as f:
            container_yaml = syaml.load_config(f)

        with open(self.base_packages, 'r') as f:
            packages_yaml = syaml.load_config(f)

        if 'packages' not in container_yaml['spack']:
            container_yaml['spack']['packages'] = {}

        container_yaml['spack']['packages'] = spack.config.merge_yaml(
            container_yaml['spack']['packages'], packages_yaml['packages'])

        container_yaml = spack.config.merge_yaml(container_yaml, app_yaml)

        os.makedirs(self.env_dir, exist_ok=True)

        with open(os.path.join(self.env_dir, 'spack.yaml'), 'w') as f:
            syaml.dump_config(container_yaml, stream=f)
