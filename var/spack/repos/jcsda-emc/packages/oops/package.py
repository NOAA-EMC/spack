# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Oops(CMakePackage):
    """Object Oriented Prediction System"""

    homepage = "https://github.com/JCSDA/oops"
    git = "https://github.com/JCSDA/oops.git"

    maintainers = ["climbfuji"]

    version("1.9.1", commit="60f93924fe446714fcb04d96f6930a760db74b23")
    version("1.8.0", commit="d9c7c74e4597172bf8a69d8585df5ad6d0112e0c")
    version("1.7.0", commit="2426c2040e9ae138c4bf8362cacca84d66bd64bf")
    version("develop", branch="develop", no_cache=True)

    variant("l95", default=True, description="Build LORENZ95 toy model")
    variant("mkl", default=False, description="Use MKL for LAPACK implementation (if available)")
    variant("openmp", default=True, description="Build oops with OpenMP support")
    variant("qg", default=True, description="Build QG toy model")
    # variant('autoprofiling', default=False,
    #         description='Enable function-based autoprofiling with GPTL (if available)')
    # variant('gptl', default=False, description='Use GPTL profiling library (if available)')

    depends_on("boost@1.64:")
    depends_on("ecbuild", type=("build"))
    depends_on("ecbuild@3.3.2:", type=("build"), when="@1.7:1.8")
    depends_on("eckit")
    depends_on("eckit@1.23.0", when="@1.7:1.8")
    depends_on("eckit@1.24.4:", when="@1.9:")
    depends_on("ecmwf-atlas")
    depends_on("ecmwf-atlas@0.33.0", when="@1.7:1.8")
    depends_on("ecmwf-atlas@0.35.0:", when="@1.9:")
    depends_on("eigen")
    depends_on("fckit")
    depends_on("fckit@0.10.1", when="@1.7:1.8")
    depends_on("fckit@0.11.0:", when="@1.9:")
    # depends_on('gptl', when='+gptl')
    depends_on("jedi-cmake", type=("build"))
    depends_on("lapack", when="~mkl")
    depends_on("llvm-openmp", when="+openmp %apple-clang", type=("build", "link", "run"))
    depends_on("mkl", when="+mkl")
    depends_on("mpi")
    depends_on("netcdf-c+mpi")
    depends_on("netcdf-fortran")
    depends_on("nlohmann-json")
    depends_on("nlohmann-json-schema-validator")

    def cmake_args(self):
        res = [
            self.define_from_variant("ENABLE_LORENZ95_MODEL", "l95"),
            self.define_from_variant("ENABLE_QG_MODEL", "qg"),
            self.define_from_variant("ENABLE_MKL", "mkl"),
            self.define_from_variant("OPENMP", "openmp"),
        ]
        return res
