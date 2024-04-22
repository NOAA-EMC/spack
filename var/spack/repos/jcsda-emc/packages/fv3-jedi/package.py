# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fv3Jedi(CMakePackage):
    """Interface between JEDI and FV3 based models"""

    homepage = "https://github.com/JCSDA/fv3-jedi"
    git = "https://github.com/JCSDA/fv3-jedi.git"

    maintainers = ["climbfuji"]

    version("develop", branch="develop", no_cache=True)
    version("1.8.0", commit="8a4974fa03b7abd267497313cd765fed08bc2623")
    version("1.7.0", commit="75fa0544ae7c6b5446460bef8cb7663f3fe1acad")
    version("1.6.0", commit="3c20ebd2657d4b8df35103207a1e83535b67469c")

    variant(
        "forecast_model",
        default="FV3CORE",
        description="fv3 forecast model",
        values=("FV3CORE", "GEOS", "UFS"),
    )
    variant("geos-aero", default=False, description="Enable usage of geos-aero")
    variant("gsibec", default=True, description="FV3-SABER block GSI")
    # Note that the option for openmp is lazily written in fv3-jedi.
    # It just enables a find_package call. If a package is already found, for example by
    # one of the package dependencies, then that component is silently used even if the user
    # toggles it off. This is a bug and should be fixed eventually.
    variant("openmp", default=True, description="Build with OpenMP support")
    variant("ropp", default=False, description="Enable usage of ropp")
    variant("sp", default=True, description="Enable usage of ncep-sp")

    conflicts("forecast_model=GEOS", msg="FV3-JEDI: GEOS to be implemented.")
    conflicts("forecast_model=UFS", msg="FV3-JEDI: UFS to be implemented.")
    conflicts("+geos-aero", msg="FV3-JEDI: geos-aero to be implemented.")
    # Note: the ropp code needs a JCSDA-internal repository.
    conflicts("+ropp", msg="FV3-JEDI: ropp to be implemented.")

    # Required components
    depends_on("crtm")
    depends_on("crtm@2.2.3:", when="@:1.5")
    depends_on("crtm@v3.0.0-skylabv5-1", when="@1.6")
    depends_on("crtm@v3.0.0-skylabv6", when="@1.7")
    depends_on("crtm@v3.1.0-skylabv7", when="@1.8")
    depends_on("ecbuild", type=("build"))
    depends_on("ecbuild@3.3.2:", type=("build"), when="@1.6:")
    depends_on("ecmwf-atlas")
    depends_on("ecmwf-atlas@0.33.0", when="@1.6:1.7")
    depends_on("ecmwf-atlas@0.35.0:", when="@1.8:")
    depends_on("femps@1.0.0:")
    depends_on("jedi-cmake", type=("build"))
    depends_on("mpi")
    # fv3-jedi depends on netcdf-fortran, which always depends on netcdf-c. However, netcdf-c
    # has the mpi options, and netcdf-fortran does not.
    depends_on("netcdf-fortran")
    depends_on("netcdf-c+mpi")
    depends_on("oops")
    depends_on("oops@1.7", when="@1.6")
    depends_on("oops@1.8", when="@1.7")
    depends_on("oops@1.9:", when="@1.8")
    depends_on("saber")
    depends_on("saber@1.7", when="@1.6")
    depends_on("saber@1.8", when="@1.7")
    depends_on("saber@1.9", when="@1.8")
    depends_on("ufo")
    depends_on("ufo@1.7", when="@1.6")
    depends_on("ufo@1.8", when="@1.7")
    depends_on("ufo@1.9", when="@1.8")
    depends_on("vader")
    depends_on("vader@1.4", when="@1.6")
    depends_on("vader@1.5", when="@1.7")
    depends_on("vader@1.6", when="@1.8")

    depends_on("fms@release-jcsda", when="forecast_model=FV3CORE")
    depends_on("fv3-jedi-linearmodel", when="forecast_model=FV3CORE")
    depends_on("fv3-jedi-linearmodel@1.2", when="@1.6 forecast_model=FV3CORE")
    depends_on("fv3-jedi-linearmodel@1.3", when="@1.7 forecast_model=FV3CORE")
    depends_on("fv3-jedi-linearmodel@1.4", when="@1.8 forecast_model=FV3CORE")

    # Optional components
    depends_on("GFDL_atmos_cubed_sphere", when="forecast_model=FV3CORE")
    depends_on("gsibec", when="+gsibec")
    depends_on("gsibec@1.1.2:", when="@1.6: +gsibec")
    depends_on("llvm-openmp", when="+openmp %apple-clang", type=("build", "link", "run"))
    depends_on("sp", when="+sp")

    def cmake_args(self):
        res = [
            self.define_from_variant("FV3_FORECAST_MODEL", "forecast_model"),
            self.define_from_variant("OPENMP", "openmp"),
        ]
        return res

    # find_package(ecbuild REQUIRED) is needed when using ecbuild.
    patch("CMakeLists.txt.16.patch", when="@1.6:1.7")
    # Same as above (different line numbers), and addressing a missing UFO
    # variable by disabling tests.
    patch("CMakeLists.txt.18.patch", when="@1.8")
    # fv3-jedi is improperly including git_functions.cmake via an environment variable.
    # It should instead use the jedicmake_FUNCTIONS variable, which is exported by jedi-cmake.
    # Addressed by fv3-jedi test refactoring that occurred after the v1.7 release.
    patch("test.CMakeLists.txt.patch", when="@1.6:1.7")
    # fv3-jedi depends on these macros that are defined (and not exported) in ufo.
    patch("cmake.fv3jedi_extra_macros.cmake.patch", when="@1.6:1.8")
