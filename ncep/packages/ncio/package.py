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
#     spack install ncio
#
# You can edit this file again by typing:
#
#     spack edit ncio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ncio(CMakePackage):
    """
    This is a library used by NCEP GSI system to read the GFS forecast files for use in data assimilation. It is also used by enkf_chgres_recenter_nc, which will read in a template output file, an input file, and regrid the input file to the template output file resolution.
    """
    

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-ncio"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-ncio/archive/refs/tags/v1.0.0.tar.gz"

    maintainers = ['kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']
    
    version('1.0.0', sha256='2e2630b26513bf7b0665619c6c3475fe171a9d8b930e9242f5546ddf54749bd4')

    depends_on('mpi')
    depends_on('netcdf-fortran')
