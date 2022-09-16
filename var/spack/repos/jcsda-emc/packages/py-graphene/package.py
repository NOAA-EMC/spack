# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGraphene(PythonPackage):
    """Graphene is an opinionated Python library for building GraphQL schemas/types fast and easily.."""

    homepage = "https://github.com/graphql-python/graphene"
    pypi     = "graphene/graphene-3.1.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('3.1', sha256='73332510a14b94fcb925dae4563ad6a028d414144704fdcc191565af72608798')

    depends_on('py-setuptools', type='build')
