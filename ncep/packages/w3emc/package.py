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
#     spack install w3emc
#
# You can edit this file again by typing:
#
#     spack edit w3emc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class W3emc(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-w3emc"
    #url      = "https://github.com/NOAA-EMC/NCEPLIBS-w3emc/archive/refs/tags/v2.7.3.tar.gz"
    git = "https://github.com/NOAA-EMC/NCEPLIBS-w3emc.git"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.7.3', tag='v2.7.3', submodules=True)

    depends_on('nemsio')
    depends_on('sigio')
    depends_on('netcdf-fortran')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
