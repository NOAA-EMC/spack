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
#     spack install jasper
#
# You can edit this file again by typing:
#
#     spack edit jasper
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Jasper(CMakePackage):
    """
    JasPer is a software toolkit for the handling of image data. The software provides a means for representing images, and facilitates
    the manipulation of image data, as well as the import/export of such
    data in numerous formats (e.g., JPEG-2000 JP2, JPEG, PNM, BMP, Sun
    Rasterfile, and PGX).
    """

    homepage = "https://jasper-software.github.io/jasper/"
    url      = "https://github.com/jasper-software/jasper/archive/refs/tags/version-2.0.32.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.0.32', sha256='a3583a06698a6d6106f2fc413aa42d65d86bedf9a988d60e5cfa38bf72bc64b9')
