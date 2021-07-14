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
#     spack install nceplibs-g2c
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-g2c
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class G2c(CMakePackage):
    """This library contains C decoder/encoder routines for GRIB edition 2."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-g2c"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/refs/tags/v1.6.2.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    variant('png', default=True)
    variant('jasper', default=True)
    variant('openjpeg', default=False)

    version('1.6.2', sha256='b5384b48e108293d7f764cdad458ac8ce436f26be330b02c69c2a75bb7eb9a2c')

    depends_on('libpng', when='+png')
    depends_on('jasper', when='+jasper')
    depends_on('openjpeg', when='+openjpeg')

    def cmake_args(self):
        args = []
        return args
