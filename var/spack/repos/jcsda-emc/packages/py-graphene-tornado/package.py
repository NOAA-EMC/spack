# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGrapheneTornado(PythonPackage):
    """A project for running Graphene on top of Tornado in Python 2 and 3.
    The codebase is a port of graphene-django."""

    homepage = "https://github.com/graphql-python/graphene-tornado"
    pypi     = "graphene-tornado/graphene-tornado-2.6.1.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('2.6.1', sha256='953bf812267177224ce1ac2a93c669069d85a8fa187a9fac681b76b63dffebc2')

    depends_on('python@3.6:')

    depends_on('py-setuptools', type='build')

    depends_on('py-six', type=('build', 'run'))
    depends_on('py-graphene', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-tornado', type=('build', 'run'))
    depends_on('py-werkzeug', type=('build', 'run'))
