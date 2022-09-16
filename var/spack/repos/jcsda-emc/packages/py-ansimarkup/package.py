# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyAnsimarkup(PythonPackage):
    """Ansimarkup is an XML-like markup for producing colored terminal text."""

    homepage = "https://github.com/gvalkov/python-ansimarkup"
    pypi     = "ansimarkup/ansimarkup-1.5.0.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('1.5.0', sha256='96c65d75bbed07d3dcbda8dbede8c2252c984f90d0ca07434b88a6bbf345fad3')

    depends_on('py-setuptools', type='build')
