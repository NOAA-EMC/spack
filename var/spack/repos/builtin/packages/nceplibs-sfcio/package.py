# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NceplibsSfcio(CMakePackage):
    """ API for surface files I/O. This is part of the NCEPLIBS project."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-sfcio/archive/refs/tags/v1.4.1.tar.gz"

    maintainers = ['edwardhartnett', 'kgerheiser', 'Hang-Lei-NOAA']    

    version('1.4.1', sha256='d9f900cf18ec1a839b4128c069b1336317ffc682086283443354896746b89c59')


