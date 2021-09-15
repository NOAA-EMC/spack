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
#     spack install nceplibs-gfsio
#
# You can edit this file again by typing:
#
#     spack edit nceplibs-gfsio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gfsio(CMakePackage):
    """
    API to convert GFS Gaussian output into grib output. This is part
    of the NCEPLIBS project.

    """
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-gfsio"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-gfsio/archive/refs/tags/v1.4.1.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    version('1.4.1', sha256='eab106302f520600decc4f9665d7c6a55e7b4901fab6d9ef40f29702b89b69b1')
    version('1.4.0', sha256='f9a605e5a8b1570b0f1cfb79c9a632386a5bb985f3783edbbd42fdbc2dc9c0c4')
