# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Mapl(CMakePackage):
    """
    MAPL is a foundation layer of the GEOS architecture, whose
    original purpose is to supplement the Earth System Modeling
    Framework (ESMF).  MAPL fills in missing capabilities of ESMF,
    provides higher-level interfaces for common boiler-plate logic,
    and enforces various componentization conventions across ESMF
    gridded components within GEOS.

    """

    homepage = "https://github.com/GEOS-ESM/MAPL"
    url      = "https://github.com/GEOS-ESM/MAPL/archive/refs/tags/v2.8.1.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('2.8.1', sha256='a7657d4c52a66c3a6663e436d2c2dd4dbb81addd747e1ace68f59843665eb739')
    version('2.8.0', sha256='6da60a21ab77ecebc80575f25b756c398ef48f635ab0b9c96932a1d4ebd8b4a0')
    version('2.7.3', sha256='e8cdc0816471bb4c42673c2fa66d9d749f5a18944cd31580a2d6fd6d961ba163')
    version('2.7.2', sha256='8f123352c665c434a18ff87304a71a61fb3342919adcccfea2a40729992d9f93')
    version('2.7.1', sha256='8239fdbebd2caa47a232c24927f7a91196704e35c8b7909e1bbbefccf0647ea6')

    resource(
        name='esma_cmake',
        git='https://github.com/GEOS-ESM/ESMA_cmake.git',
        tag='v3.4.3')

    resource(
        name='CMakeModules',
        git='https://github.com/NOAA-EMC/CMakeModules.git',
        tag='v1.2.0')

    variant('flap', default=False)
    variant('pflogger', default=False)
    variant('esma_gfe_namespace', default=True)
    variant('shared', default=True)

    depends_on('hdf5')
    depends_on('netcdf-c')
    depends_on('esmf')
    depends_on('yafyaml')
    depends_on('gftl-shared')
    depends_on('ecbuild')

    def cmake_args(self):
        dir = os.getcwd()
        ecbuild_prefix = self.spec["ecbuild"].prefix
        args = [
            self.define_from_variant('BUILD_WITH_FLAP', 'flap'),
            self.define_from_variant('BUILD_WITH_PFLOGGER', 'pflogger'),
            self.define_from_variant('ESMA_USE_GFE_NAMESPACE', 'esma_gfe_namespace'),
            self.define_from_variant('BUILD_SHARED_MAPL', 'shared'),
            '-DCMAKE_MODULE_PATH={pwd}/ESMA_cmake;{pwd}/CMakeModules/Modules;' +
            '{ecbuild_prefix}/share/ecbuild/cmake'.format(pwd=dir,
                                                          ecbuild_prefix=ecbuild_prefix),
            '-DCMAKE_Fortran_FLAGS=-ffree-line-length-none'
        ]

        return args
