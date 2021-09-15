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
#     spack install nceplibs-w3nco
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-w3nco
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class W3nco(CMakePackage):
    """
    This library contains Fortran 90 decoder/encoder routines for GRIB edition 1.
    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-w3nco"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-w3nco/archive/refs/tags/v2.4.1.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.4.1', sha256='48b06e0ea21d3d0fd5d5c4e7eb50b081402567c1bff6c4abf4fd4f3669070139')
