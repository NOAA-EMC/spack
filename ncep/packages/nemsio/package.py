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
#     spack install nceplibs-nemsio
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-nemsio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nemsio(CMakePackage):
    """
    Performs I/O for the NCEP models using NEMS.
    This is part of the NCEPLIBS project. 
    """

    # FIXME: Add a proper url for your package's homepage here.
    homfepage = "https://github.com/NOAA-EMC/NCEPLIBS-nemsio"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-nemsio/archive/refs/tags/v2.5.2.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.5.2', sha256='c59e9379969690de8d030cbf4bbbbe3726faf13c304f3b88b0f6aec1496d2c08')

    depends_on('w3nco')
    depends_on('bacio')
