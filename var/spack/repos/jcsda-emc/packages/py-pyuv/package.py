# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyuv(PythonPackage):
    """pyuv is a Python module which provides an interface to libuv.
    libuv is a high performance asynchronous networking and platform abstraction library."""

    homepage = "https://github.com/saghul/pyuv"
    pypi     = "pyuv/pyuv-1.4.0.tar.gz"

    maintainers = ['kgerheiser', 'climbfuji']

    version('1.4.0', sha256='caea2004d1125fe17cbde3c211c8abc72844e9b8dd7dfa007711e98fbc96fbc2')

    depends_on('py-setuptools', type='build')
