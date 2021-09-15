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
#     spack install cdo
#
# You can edit this file again by typing:
#
#     spack edit cdo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cdo(AutotoolsPackage):
    """CDO is a collection of command line Operators to manipulate and
    analyse Climate and NWP model Data.  Supported data formats are
    GRIB 1/2, netCDF 3/4, SERVICE, EXTRA and IEG.  There are more than
    600 operators available.

    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://code.mpimet.mpg.de/projects/cdo"
    url      = "https://code.mpimet.mpg.de/attachments/download/20826/cdo-1.9.8.tar.gz"

    maintainers = ['kgerheiser']

    version('1.9.8', sha256='f2660ac6f8bf3fa071cf2a3a196b3ec75ad007deb3a782455e80f28680c5252a')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
