# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import sys

from spack import *


class GlobalWorkflowEnv(BundlePackage):
    """Development environment for GSI"""

    homepage = "https://github.com/NOAA-EMC/GSI"
    git      = "https://github.com/NOAA-EMC/global-workflow.git"

    maintainers = ['kgerheiser']

    version('develop', branch='develop')

    depends_on('netcdf-fortran')
    depends_on('bacio')
    depends_on('g2')
    depends_on('w3nco')
    depends_on('w3emc')
    depends_on('sp')
    depends_on('ip')
    depends_on('nemsio')
    depends_on('nemsiogfs')
    depends_on('ncio')
    depends_on('landsfcutil')
    depends_on('sigio')
    depends_on('bufr')
    depends_on('wgrib2')
