# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Parallelio(CMakePackage):
    """The Parallel IO libraries (PIO) are high-level parallel I/O C and
    Fortran libraries for applications that need to do netCDF I/O from
    large numbers of processors on a HPC system."""

    homepage = "https://ncar.github.io/ParallelIO/"
    url      = "https://github.com/NCAR/ParallelIO/archive/pio2_5_4.tar.gz"

    maintainers = ['tkameyama']

    version('2_5_4', sha256='34fa8c74bfb316e8cb626a3c02e6bc3b99eb51c0f2d5589776e4c15fdbcf7c68')
    version('2_5_3', sha256='63ae300d7b2e8790a272d442cb2856ff053810a05a9c37d28228fc4ebde1f5f5')
    version('2_5_2', sha256='378e6d01dbfb9e99a913be814d3a4f04f93a3bb9f860468ccaf199ed3687acac')
    version('2_5_0', sha256='685cfe16d5d308b65e86242bcb8acafdfabd1bf4bff964789745c79caea9dca1')

    variant('pnetcdf', default=False, description='enable pnetcdf')
    
    depends_on('mpi')
    depends_on('netcdf-c +mpi', type='link')
    depends_on('netcdf-fortran', type='link')
    depends_on('parallel-netcdf', type='link', when='+pnetcdf')

    resource(name='CMake_Fortran_utils',
             git='https://github.com/CESM-Development/CMake_Fortran_utils.git',
             tag='master')
    resource(name='genf90',
             git='https://github.com/PARALLELIO/genf90.git',
             tag='genf90_200608')

    def cmake_args(self):
        define = self.define
        spec = self.spec
        env['CC'] = spec['mpi'].mpicc
        env['FC'] = spec['mpi'].mpifc
        src = self.stage.source_path
        args = [
            define('NetCDF_C_PATH', spec['netcdf-c'].prefix),
            define('NetCDF_Fortran_PATH', spec['netcdf-fortran'].prefix),
            define('USER_CMAKE_MODULE_PATH', join_path(src, 'CMake_Fortran_utils')),
            define('GENF90_PATH', join_path(src, 'genf90')),
        ]
        if spec.satisfies('+pnetcdf'):
            args.extend([
                define('PnetCDF_C_PATH', spec['parallel-netcdf'].prefix),
                define('PnetCDF_Fortran_PATH', spec['parallel-netcdf'].prefix),
            ])
        return args
