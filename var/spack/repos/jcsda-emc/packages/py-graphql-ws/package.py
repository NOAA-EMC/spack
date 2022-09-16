# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGraphqlWs(PythonPackage):
    """Websocket backend for GraphQL subscriptions."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/graphql-python/graphql-ws"
    pypi     = "graphql-ws/graphql-ws-0.4.4.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('0.4.4', sha256='2ad38db70f37964f54d7eb3e2ede86dbe3f2a1ed7ea0a9f9a3b8b17162a22852')

    depends_on('py-setuptools', type='build')

    depends_on('py-graphql-core', type=('build', 'run'))
