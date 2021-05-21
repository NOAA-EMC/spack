# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NceplibsSp(CMakePackage):
    """The spectral transform library (splib) contains FORTRAN
    subprograms to be used for a variety of spectral transform
    functions. This is part of the NCEPLIBS project.

    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-sp"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-sp/archive/refs/tags/v2.3.3.tar.gz"

    maintainers = ['edwardhartnett', 'kgerheiser', 'Hang-Lei-NOAA']

    version('2.3.3', sha256='c0d465209e599de3c0193e65671e290e9f422f659f1da928505489a3edeab99f')


