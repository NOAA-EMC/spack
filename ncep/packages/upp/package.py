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
#     spack install upp
#
# You can edit this file again by typing:
#
#     spack edit upp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Upp(CMakePackage):
    """
    The Unified Post Processor (UPP) software package is a software
    package designed to generate useful products from raw model
    output.

    """

    homepage = "https://github.com/NOAA-EMC/EMC_post"
    url      = "https://github.com/NOAA-EMC/EMC_post/archive/refs/tags/upp_v10.0.8.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    git = "https://github.com/NOAA-EMC/EMC_post.git"

    version('10.0.8', tag='upp_v10.0.8', submodules=True)
    version('10.0.7', tag='upp_v10.0.7', submodules=True)
    version('10.0.6', tag='upp_v10.0.6', submodules=True)
    version('10.0.5', tag='upp_v10.0.5', submodules=True)
    version('10.0.4', tag='upp_v10.0.4', submodules=True)
    version('10.0.3', tag='upp_v10.0.3', submodules=True)

    variant('openmp', default=True)
    variant('postexec', default=True)
    variant('wrf_io', default=False)
    variant('docs', default=False)

    depends_on('mpi')
    depends_on('netcdf-fortran')
    depends_on('bacio')
    depends_on('crtm')
    depends_on('g2')
    depends_on('g2tmpl')
    depends_on('ip')

    depends_on('nemsio', when='+postexec')
    depends_on('sfcio', when='+postexec')
    depends_on('sigio', when='+postexec')
    depends_on('sp', when='+postexec')
    depends_on('w3nco', when='+postexec')
    depends_on('wrf_io', when='+wrf_io')
    depends_on('doxygen', when='+docs')

    def cmake_args(self):
        args = [
            self.define_from_variant('OPENMP', 'openmp'),
            self.define_from_variant('BUILD_POSTEXEC', 'postexec'),
            self.define_from_variant('BUILD_WITH_WRFIO', 'wrf_io'),
            self.define_from_variant('ENABLE_DOCS', 'docs')
        ]

        return args
