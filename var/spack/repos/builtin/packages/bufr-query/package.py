# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class BufrQuery(CMakePackage):
    """The NOAA bufr-query Library can be used to read NCEP and WMO formated BUFR
       files using a simple interface that does not require the user to know the
       details of the BUFR format.
       
       Detailed documentation for the BUFR Library can be found at
       https://bufr-query.readthedocs.io/en/latest/index.html"""

    homepage = "https://github.com/NOAA-EMC/bufr-query"
    url = "https://github.com/NOAA-EMC/bufr-query/archive/refs/tags/v0.0.1.tar.gz"
    maintainers("srherbener", "rmclaren")

    license("Apache-2.0", checked_by="srherbener")

    version("0.0.1", sha256="001990d864533c101b93d1c351edf50cf8b5ccc575e442d174735f6c332d3d03")

    # Required dependencies
    depends_on("llvm-openmp", type=("build", "run"))
    depends_on("mpi", type=("build", "run"))
    depends_on("eckit@1.24.4:", type=("build", "run"))
    depends_on("eigen@3:", type=("build", "run"))
    depends_on("gsl-lite", type=("build", "run"))
    depends_on("netcdf-cxx", type=("build", "run"))

    # Optional dependencies
    variant("python", default=False, description="Enable Python interface")
    depends_on("python@3:", type=("build", "run"), when="+python")
    depends_on("py-pybind11", type=("build"), when="+python")

    # CMake configuration
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_PYTHON_BINDINGS", "python")
        ]
        return args
