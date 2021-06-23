# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install jasper
#
# You can edit this file again by typing:
#
#     spack edit jasper
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Jasper(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/jasper-software/jasper/archive/refs/tags/version-2.0.32.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.0.32', sha256='a3583a06698a6d6106f2fc413aa42d65d86bedf9a988d60e5cfa38bf72bc64b9')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
