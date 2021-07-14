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
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/jasper-software/jasper/archive/refs/tags/version-2.0.32.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.0.32', sha256='19ece30c1f94a44b3deda62f0ffbc7f8e81458b709640b80365234979c538068')
    version('2.0.31', sha256='d419baa2f8a6ffda18472487f6314f0f08b673204723bf11c3a1f5b3f1b8e768')
    version('2.0.29', sha256='89a0c02df996090e07ff512002d534a1d56a567be7a6422fc6fc6ba79bd500e7')
    version('2.0.28', sha256='6b4e5f682be0ab1a5acb0eeb6bf41d6ce17a658bb8e2dbda95de40100939cc88')
    version('2.0.27', sha256='df41bd015a9dd0cc2a2e696f8ca5cbfb633323ca9429621f7fa801778681f2dd')
    version('2.0.26', sha256='a82a119e85b7d1f448e61309777fa5f79053a9adca4a2b5bfe44be5439fb8fea')
    version('2.0.25', sha256='f5bc48e2884bcabd2aca1737baff4ca962ec665b6eb673966ced1f7adea07edb')
    version('2.0.24', sha256='d2d28e115968d38499163cf8086179503668ce0d71b90dd33855b3de96a1ca1d')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
