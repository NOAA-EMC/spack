# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class GeosPyenv(BundlePackage):
    """
    Python development environment for NASA GEOS.
    """

    homepage = ""
    # There is no URL since there is no code to download.

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA']

    version('1.0.0')

    depends_on('py-isodate')
    depends_on('py-pycodestyle')
    depends_on('py-xarray')
    depends_on('py-cartopy')
    depends_on('py-scikiy-learn')
    depends_on('py-netcdf4')
    # There is no need for install() since there is no code.
