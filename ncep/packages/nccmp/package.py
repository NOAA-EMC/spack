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
#     spack install nccmp
#
# You can edit this file again by typing:
#
#     spack edit nccmp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nccmp(CMakePackage):
    """
    Compare two NetCDF files
    """

    homepage = "https://gitlab.com/remikz/nccmp"
    url      = "https://gitlab.com/remikz/nccmp/-/archive/1.8.9.0/nccmp-1.8.9.0.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA']

    version('1.8.9.0', sha256='da5d2b4dcd52aec96e7d96ba4d0e97efebbd40fe9e640535e5ee3d5cd082ae50')
    version('1.8.8.0', sha256='6b5e1655cef551b1484df94a097a3b1d5d9209314ad123fa2f562472d6ea52d7')
    version('1.8.7.0', sha256='a864c4724200d005bf8bc925da717ef7c69b0b0a14730c09540e5a86daad8988')

    depends_on('netcdf-c')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
