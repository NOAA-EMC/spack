# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCylcUiserver(PythonPackage):
    """This project contains the Cylc UI Server which provides the Cylc GUI
    used to serve the Cylc UI, and to communicate with running Cylc Schedulers."""

    homepage = "https://cylc.github.io"
    pypi     = "cylc-uiserver/cylc-uiserver-1.0.3.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('1.0.3', sha256='a94560102656dc5e637b839139590403ee30e1e4abb61446cbdc5bfd33a3efb5')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('py-cylc-flow', type=('build', 'run'))
    depends_on('py-tornado', type=('build', 'run'))
    depends_on('py-traitlets', type=('build', 'run'))
    depends_on('py-rx', type=('build', 'run'))
    depends_on('py-graphene', type=('build', 'run'))
    depends_on('py-graphql-ws', type=('build', 'run'))
    depends_on('py-graphene-tornado', type=('build', 'run'))
    depends_on('py-jupyter-server', type=('build', 'run'))
