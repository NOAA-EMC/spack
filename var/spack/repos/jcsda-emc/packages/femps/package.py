# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Femps(CMakePackage):
    """Finite Element Mesh Poisson Solver"""

    homepage = "https://github.com/JCSDA/femps"
    git = "https://github.com/JCSDA/femps.git"

    maintainers = ["climbfuji"]

    version("1.2.0", commit="a22e458c1742695479db9011ddb6bcbf31de39fe")

    depends_on("ecbuild", type=("build"))
    depends_on("ecbuild@3.3.2:", type=("build"), when="@1.7.0:")
    depends_on("jedi-cmake", type=("build"))
    depends_on("llvm-openmp", when="%apple-clang", type=("build", "run"))
    depends_on("mpi")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")

    # find_package(ecbuild REQUIRED) is needed when using ecbuild.
    patch("CMakeLists.txt.patch", when="@1.2.0")
    # femps needs to install its Fortran modules.
    patch("src.femps.CMakeLists.txt.patch", when="@1.2.0")
