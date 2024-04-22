# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fv3JediLinearmodel(CMakePackage):
    """Tangent linear and adjoint versions of FV3 dynamical core and GEOS physics"""

    homepage = "https://github.com/JCSDA/fv3-jedi-linearmodel"
    git = "https://github.com/JCSDA/fv3-jedi-linearmodel.git"

    maintainers = ["climbfuji"]

    version("1.4.0", commit="05cc1ae63252ca535f3db0fdca9a8a996329fc8f")
    version("1.3.0", commit="9758fbd44166fc1e1d745ca9ab7e9e5e6071955f")
    version("1.2.0", commit="d47cea97c659e8a11e9e64c23092bef06227ebde")
    version("develop", branch="develop", no_cache=True)

    variant(
        "forecast_model",
        default="FV3CORE",
        description="fv3 forecast model",
        values=("FV3CORE", "GEOS", "UFS"),
    )
    # Note that the options for mkl, mpi, and openmp are lazily written in fv3-jedi-linearmodel.
    # These options just turn on a find_package call. If a package is already found, for example by
    # one of the package dependencies, then that component is silently used even if the user
    # toggles it off. This is a bug and should be fixed eventually.
    variant("mkl", default=False, description="Use MKL for LAPACK implementation (if available)")
    variant("mpi", default=True, description="Support for MPI distributed parallelism")
    variant("openmp", default=True, description="Build with OpenMP support")

    conflicts("forecast_model=GEOS", msg="FV3-JEDI-LINEARMODEL: GEOS to be implemented.")
    conflicts("forecast_model=UFS", msg="FV3-JEDI-LINEARMODEL: UFS to be implemented.")

    depends_on("ecbuild", type=("build"))
    depends_on("ecbuild@3.3.2:", type=("build"), when="@1.7.0:")
    depends_on("fms@release-jcsda", when="forecast_model=FV3CORE")
    depends_on("fms@release-jcsda", when="forecast_model=UFS")
    depends_on("jedi-cmake", type=("build"))
    depends_on("lapack", when="~mkl")
    depends_on("llvm-openmp", when="+openmp %apple-clang", type=("build", "link", "run"))
    depends_on("mkl", when="+mkl")
    depends_on("mpi", when="+mpi")
    depends_on("netcdf-fortran")
    depends_on("netcdf-c~mpi", when="~mpi")
    depends_on("netcdf-c+mpi", when="+mpi")

    # Future: GEOS needs
    # - MAPL (underway at GMAO)
    # - GEOSgcm
    # - fms r8 or r4

    # Future: UFS needs
    # - stochastic_physics
    # - ccpp
    # - ccppphys
    # - fv3atm
    # - ufs
    # - FMS::fms_r8

    def cmake_args(self):
        res = [self.define_from_variant("FV3_FORECAST_MODEL", "forecast_model")]
        return res

    # find_package(ecbuild REQUIRED) is needed when using ecbuild.
    patch("CMakeLists.txt.patch", when="@1.2:1.4")
    # fv3-jedi-linearmodel needs to install its Fortran modules.
    patch("src.CMakeLists.txt.patch", when="@1.2:1.4")
