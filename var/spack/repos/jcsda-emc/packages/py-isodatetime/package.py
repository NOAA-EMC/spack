# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIsodatetime(PythonPackage):
    """Python ISO8601 (2004) full-specification parser and data model/manipulation utilities.
    Intended to be used in a similar way to Python's datetime module."""

    homepage = "https://github.com/metomi/isodatetime"

    # PyPI URL has an exclamation (!) in it which confuses Spack, so use Github
    url      = "https://github.com/metomi/isodatetime/archive/refs/tags/3.0.0.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('3.0.0', sha256='ecf592e10ceef68ff31df79b909f919383752b57308299f6fc8b8d2ce8471d15')

    depends_on('python@3.6:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')
