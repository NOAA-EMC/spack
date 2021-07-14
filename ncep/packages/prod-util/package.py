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
#     spack install prod-util
#
# You can edit this file again by typing:
#
#     spack edit prod-util
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class ProdUtil(CMakePackage):
    """
    Product utilities for the NCEP models. This is part of the NCEPLIBS project.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-prod_util"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-prod_util/archive/refs/tags/v1.2.2.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']
    
    version('1.2.2', sha256='c51b903ea5a046cb9b545b5c04fd28647c58b4ab6182e61710f0287846350ef8')

    depends_on('w3nco')
