# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCylcFlow(PythonPackage):
    """Cylc (pronounced silk) is a general purpose workflow engine that specialises
    in cycling workflows and has strong scaling characteristics"""

    homepage = "https://cylc.github.io"
    pypi     = "cylc-flow/cylc-flow-8.0rc3.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('8.0rc3', sha256='20f244879d35e7e574aacf8e92149a84f43a44cb88f240cf02d0204bb2b3d27a')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('py-aiofiles', type=('build', 'run'))
    depends_on('py-ansimarkup', type=('build', 'run'))
    depends_on('py-graphene', type=('build', 'run'))
    depends_on('py-isodatetime', type=('build', 'run'))
    depends_on('py-pyuv', type=('build', 'run'))
    depends_on('py-async-timeout', type=('build', 'run'))
    depends_on('py-colorama', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-protobuf', type=('build', 'run'))
    depends_on('py-psutil', type=('build', 'run'))
    depends_on('py-pyzmq', type=('build', 'run'))
    depends_on('py-urwid@2:', type=('build', 'run'))
    depends_on('py-rx', type=('build', 'run'))
    depends_on('py-promise', type=('build', 'run'))
    depends_on('py-markupsafe', type=('build', 'run'))

    def global_options(self, spec, prefix):
        options = []
        return options

    def install_options(self, spec, prefix):
        options = []
        return options
