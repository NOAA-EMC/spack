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
#     spack install wrf-io
#
# You can edit this file again by typing:
#
#     spack edit wrf-io
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class WrfIo(CMakePackage):
    """    
    This is a lightweight WRF-IO API library for Unified Post Processor (UPP). 
    It reads wrf forecasts (WRF state plus diagnostics). 
    It is based on code copied from https://github.com/wrf-model/WRF/tree/master/external/io_netcdf.
    """
    

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-wrf_io"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-wrf_io/archive/refs/tags/v1.2.0.zip"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    version('1.2.0', sha256='4a7d542f622bbed9de31c858b59f75fea77c400bc83fd3cfcb7dd2da128ac1b2')

    variant('openmp', default=False, description='Enable multithreading with OpenMP')

    depends_on('netcdf-fortran')

    def cmake_args(self):
        args = [self.define_from_variant('OPENMP', 'openmp')]
        return args
