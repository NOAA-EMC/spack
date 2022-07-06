# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import sys

from spack import *


class GlobalWorkflowEnv(BundlePackage):
    """Development environment for NOAA's Global Workflow"""

    homepage = "https://github.com/NOAA-EMC/global-workflow"
    git      = "https://github.com/NOAA-EMC/global-workflow.git"

    maintainers = ['kgerheiser']

    version('1.0.0')
    variant('python', default=True, description='Build Python dependencies')

    depends_on('ufs-pyenv', when='+python')
    depends_on('prod-util')
    depends_on('nco')
    depends_on('cdo')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('esmf')
    depends_on('nceplibs-env')
    depends_on('met')
    depends_on('metplus')

    # There is no need for install() since there is no code.
