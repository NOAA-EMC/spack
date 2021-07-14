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
#     spack install grib-util
#
# You can edit this file again by typing:
#
#     spack edit grib-util
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class GribUtil(CMakePackage):
    """
    This is a collection of NCEP GRIB related utilities. This is related to the NCEPLIBS project.
    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-grib_util"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-grib_util/archive/refs/tags/v1.2.2.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']
    
    version('1.2.2', sha256='fe9200b715de3ea2cc7007b2b09cd908e67c275cf0053caf5de848c426b8bae4')

    variant('openmp', default=False, description='Use OpenMP multithreading')

    depends_on('jasper')
    depends_on('libpng')
    depends_on('zlib')
    depends_on('w3nco')
    depends_on('g2')
    depends_on('bacio')
    depends_on('ip')
    depends_on('sp')

    def cmake_args(self):
        args = [self.define_from_variant('OPENMP', 'openmp')]
        return args
