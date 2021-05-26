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
#     spack install nceplibs-g2tmpl
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-g2tmpl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class G2tmpl(CMakePackage):
    """
    Utilities for GRIB2 template
    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-g2tmpl"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-g2tmpl/archive/refs/tags/v1.10.0.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('1.10.0', sha256='dcc0e40b8952f91d518c59df7af64e099131c17d85d910075bfa474c8822649d')
    version('1.9.1',  sha256='237e8da0add8e0392ad55b2a058b6307ff23c3dee7f5e356b261a10c0afc6823')
