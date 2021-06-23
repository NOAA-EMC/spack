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
#     spack install nceplibs-g2
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-g2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class G2(CMakePackage):
    """    
    Utilities for coding/decoding GRIB2 messages. 
    This library contains Fortran 90 decoder/encoder routines for GRIB edition 2, as well as indexing/searching utility routines. 
    This is part of the NCEPLIBS project.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-g2"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-g2/archive/refs/tags/v3.4.2.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('3.4.2', sha256='5bbd20636463bb5a86dc1a356d00351c26ee15719d6d651abd92794f299f1ab9')

    depends_on('jasper')
    depends_on('libpng')

    def cmake_args(self):
        args = []
        return args
