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
#     spack install landsfcutil
#
# You can edit this file again by typing:
#
#     spack edit landsfcutil
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Landsfcutil(CMakePackage):
    """
    Utility routines useful for initializing land-surface states in NCEP models. This is part of the NCEPLIBS project.
    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-landsfcutil"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-landsfcutil/archive/refs/tags/v2.4.1.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    version('2.4.1', sha256='831c5005a480eabe9a8542b4deec838c2650f6966863ea2711cc0cc5db51ca14')
