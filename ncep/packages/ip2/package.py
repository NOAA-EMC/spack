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
#     spack install ip2
#
# You can edit this file again by typing:
#
#     spack edit ip2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ip2(CMakePackage):
    """
    The NCEP general interpolation library 2 (ip2lib) contains Fortran 90 subprograms to be used for interpolating between nearly all grids used at NCEP. The library is particularly efficient when interpolating many fields at one time. The library has been extensively tested with AIX and Intel Fortran compilers.
    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-ip2"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-ip2/archive/refs/tags/v1.1.2.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']
    
    version('1.1.2', sha256='73c6beec8fd463ec7ccba3633d8c5d53d385c43d507367efde918c2db0af42ab')

    variant("openmp", default=False)

    depends_on('sp')

    def cmake_args(self):
        args = [
            self.define_from_variant('OPENMP', 'openmp')
        ]
        return args
