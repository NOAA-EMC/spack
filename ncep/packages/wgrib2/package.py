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
#     spack install wgrib2
#
# You can edit this file again by typing:
#
#     spack edit wgrib2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Wgrib2(CMakePackage):
    """
    Provides functionality for interacting with, reading, writing, and manipulating grib2 files.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-wgrib2"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-wgrib2/archive/refs/tags/v2.0.8-cmake-v6.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    version('2.0.8-cmake-v6', sha256='745cd008b4ce0245ea44247733e57e2b9ec6c5205d171d457e18d0ff8f87172d')

    variant('jasper', default=True)
    variant('ipolates', default=0, values=('0', '1', '3'), multi=False)
    variant('netcdf4', default=False)
    variant('regex', default=True)
    variant('tigge', default=True)
    variant('spectral', default=False)
    variant('openmp', default=False)
    variant('proj4', default=False)
    variant('wmo-validation', default=False)
    variant('timezone', default=False)
    variant('g2c', default=False)
    variant('png', default=True)
    variant('aec', default=False)
    variant('lib', default=True)
    variant('shared', default=False)

    depends_on('ip2', when='ipolates=3')
    depends_on('ip', when='ipoldates=1')
    depends_on('jasper', when='+jasper')
    depends_on('netcdf-c', when='netcdf4')
    depends_on('libpng', when='+png')

    def cmake_args(self):
        args = [
            self.define_from_variant('USE_JASPER', 'jasper'),
            self.define_from_variant('USE_IPOLATES', 'ipolates'),
            self.define_from_variant('USE_NETCDF4', 'netcdf4'),
            self.define_from_variant('USE_REGEX', 'regex'),
            self.define_from_variant('OPENMP', 'openmp'),
            self.define_from_variant('BUILD_LIB', 'lib'),
            self.define_from_variant('USE_SPECTRAL', 'spectral'),
            self.define_from_variant('USE_TIGGE', 'tigge'),
            self.define_from_variant('USE_PNG', 'png')
        ]
        return args
