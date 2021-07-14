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
#     spack install emc-crtm
#
# You can edit this file again by typing:
#
#     spack edit emc-crtm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Crtm(CMakePackage):
    homepage = "https://github.com/NOAA-EMC/EMC_crtm"
    url      = "https://github.com/NOAA-EMC/EMC_crtm/archive/refs/tags/v2.3.0.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett']

    version('2.3.0', sha256='3e2c87ae5498c33dd98f9ede5c39e33ee7f298c7317b12adeb552e3a572700ce')
