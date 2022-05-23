# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class UfsSrwEnv(BundlePackage):
    """
    Development environment for the UFS Short-Range Weather Application
    """

    homepage = "https://github.com/ufs-community/ufs-srweather-app"
    git = "https://github.com/ufs-community/ufs-srweather-app.git"
    # There is no URL since there is no code to download.

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA']

    version('develop', preferred=True)
    version('public-v2')

    with when('@develop'):
        depends_on('netcdf-fortran')
        depends_on('parallelio')
        depends_on('esmf')
        depends_on('fms')
        depends_on('bacio')
        depends_on('crtm')
        depends_on('g2')
        depends_on('g2tmpl')
        depends_on('ip')
        depends_on('sp')
        depends_on('w3nco')
        depends_on('upp')
        depends_on('gfsio')
        depends_on('landsfcutil')
        depends_on('nemsio')
        depends_on('nemsiogfs')
        depends_on('sfcio')
        depends_on('sigio')
        depends_on('w3emc')
        depends_on('wgrib2')

    with when('@public-v2'):
        depends_on('zlib@1.2.11')
        depends_on('libpng@1.6.35')
        depends_on('jasper@2.0.25')
        depends_on('hdf5@1.10.6')
        depends_on('netcdf-c@4.7.4')
        depends_on('netcdf-fortran@4.5.3')
        depends_on('fms@2021.03')
        depends_on('bacio@2.4.1')
        depends_on('crtm@2.3.0')
        depends_on('g2@3.4.3')
        depends_on('g2tmpl@1.10.0')
        depends_on('ip@3.3.3')
        depends_on('sp@2.3.3')
        depends_on('w3nco@2.4.1')
        depends_on('upp@10.0.10')
        depends_on('gftl-shared@1.3.3')
        depends_on('yafyaml@0.5.1')
        depends_on('gfsio@1.4.1')
        depends_on('landsfcutil@2.4.1')
        depends_on('nemsio@2.5.2')
        depends_on('nemsiogfs@2.5.3')
        depends_on('sfcio@1.4.1')
        depends_on('sigio@2.3.2')
        depends_on('w3emc@2.7.3')
        depends_on('wgrib2@2.0.8')
        depends_on('parallelio@2.5.2')
        depends_on('esmf@8.2.0')

    # There is no need for install() since there is no code.
