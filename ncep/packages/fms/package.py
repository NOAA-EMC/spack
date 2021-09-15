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
#     spack install fms
#
# You can edit this file again by typing:
#
#     spack edit fms
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Fms(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/NOAA-GFDL/FMS"
    url      = "https://github.com/NOAA-GFDL/FMS/archive/refs/tags/2021.02.01.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    variant('64bit', default=True, description='64 bit?')
    variant('gfs_phys', default=True, description='Use GFS Physics?')
    variant('openmp', default=True, description='Use OpenMP?')

    version('2021.02.01', sha256='9b11d9474d7c90464af66d81fb86c4798cfa309b9a0da20b0fccf33c4f65386b')
    version('2021.02',    sha256='db810b2452a6952239f064b52c0c5c58fc62126057982111b9fcd64f1b3bd879')
    version('2021.01',    sha256='38c748e2edb94ffeb021095d8bde4d74b7834610ce0ef1dbb4dce353eeb5cd96')
    version('2020.04.03', sha256='42fd28c36af16a2c63e52daa03ee0fb20837c420bd910a1e8906cf809cdce7a4')
    version('2020.04.02', sha256='bd6ce752b1018d4418398f14b9fc486f217de76bcbaaf2cdbf4c43e0b3f39f69')
    version('2020.04.01', sha256='2c409242de7dea0cf29f8dbf7495698b6bcac1eeb5c4599a728bdea172ffe37c')
    version('2020.04',    sha256='6528ef7a6bb386495c845b075c4524b4dc89093674c6410c06e5dfdaf56b781d')
    version('2020.03',    sha256='99a74c93589132290160d67f173e853bbdffcc9b7585a0d26733a992618aa43a')
    version('2020.02.01', sha256='86d9143ab13be232fddea80d9e528c3cdd6008702adb1ebe8fe4181f385896c7')
    version('2019.01.03', sha256='60a5181e883e141f2fdd4a30c535a788d609bcbbbca4af7e1ec73f66f4e58dc0')

    depends_on('netcdf-c', type='build')
    depends_on('netcdf-fortran', type='build')

    def cmake_args(self):
        args = [
            self.define_from_variant('64BIT'),
            self.define_from_variant('GFS_PHYS'),
            self.define_from_variant('OPENMP')
        ]

        args.append(self.define('CMAKE_C_COMPILER', self.spec['mpi'].mpicc))
        args.append(self.define('CMAKE_CXX_COMPILER', self.spec['mpi'].mpicxx))
        args.append(self.define('CMAKE_Fortran_COMPILER', self.spec['mpi'].mpifc))

        return args
