# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCylcRose(PythonPackage):
    """A Cylc plugin providing support for the Rose rose-suite.conf file."""

    homepage = "https://cylc.github.io"
    pypi     = "cylc-rose/cylc-rose-1.0.3.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('1.0.3', sha256='0e6f97c2e9b6192772b5c1f14f44f490d70319ceb92634485412e1dc54466dc3')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('py-cylc-flow', type=('build', 'run'))

    # Need these packages
    depends_on('py-metomi-rose', type=('build', 'run'))
    depends_on('py-metomi-isodatetime', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))

    def global_options(self, spec, prefix):
        options = []
        return options

    def install_options(self, spec, prefix):
        options = []
        return options
