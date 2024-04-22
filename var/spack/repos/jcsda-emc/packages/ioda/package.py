# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ioda(CMakePackage):
    """Interface for Observation Data Access"""

    homepage = "https://github.com/JCSDA/ioda"
    git = "https://github.com/JCSDA/ioda.git"

    maintainers = ["climbfuji"]

    version("2.8.0", commit="1ee94a863d1fc8c2752e5b95409d6742f4402f5b")
    version("2.7.0", commit="ee35b7f7f859b78e823b69d72b4bc230b15f3d46")
    version("2.6.0", commit="26abb62ca8d30cc7b84303c4d780f0f253b287c9")
    version("develop", branch="develop", no_cache=True)

    # Let's always assume IODA_BUILD_LANGUAGE_FORTRAN=on.
    # variant('fortran', default=True, description='Build the ioda Fortran interface')
    variant("odc", default=True, description="Build ODC bindings")
    # ioda has no explicit OpenMP calls, but header files from Eigen and oops do use openmp.
    variant("openmp", default=True, description="Build with OpenMP support")
    # Let's always BUILD_PYTHON_BINDINGS.
    # variant('python', default=True, description='Build the ioda Python interface')

    depends_on("boost@1.64.0:")
    depends_on("ecbuild", type=("build"))
    depends_on("eckit")
    depends_on("eckit@1.23.0:", when="@2.6:")
    depends_on("eigen")
    depends_on("fckit")
    depends_on("fckit@0.10.1:", when="@2.6:")
    depends_on("gsl-lite")
    depends_on("hdf5@1.12.0: +mpi")
    depends_on("hdf5@1.14.0: +mpi", when="@2.6.0:")
    depends_on("jedi-cmake", type=("build"))
    depends_on("llvm-openmp", when="+openmp %apple-clang", type=("build", "link", "run"))
    depends_on("mpi")
    depends_on("odc", when="+odc")
    depends_on("odc@1.0.2:", when="@2.6: +odc")
    depends_on("odc@1.4.6:", when="@2.8: +odc")
    depends_on("oops+openmp", when="+openmp")
    depends_on("oops~openmp", when="~openmp")
    depends_on("oops@1.7", when="@2.6")
    depends_on("oops@1.8", when="@2.7")
    depends_on("oops@1.9", when="@2.8:")
    depends_on("python@3.7:")
    depends_on("py-pybind11")
    depends_on("udunits@2.2.0:")
