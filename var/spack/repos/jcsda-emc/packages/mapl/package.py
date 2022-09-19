# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mapl(CMakePackage):
    """
    MAPL is a foundation layer of the GEOS architecture, whose
    original purpose is to supplement the Earth System Modeling
    Framework (ESMF).  MAPL fills in missing capabilities of ESMF,
    provides higher-level interfaces for common boiler-plate logic,
    and enforces various componentization conventions across ESMF
    gridded components within GEOS.

    """

    homepage = "https://github.com/GEOS-ESM/MAPL"
    url      = "https://github.com/GEOS-ESM/MAPL/archive/refs/tags/v2.17.1.tar.gz"
    git      = "https://github.com/GEOS-ESM/MAPL.git"

    maintainers = ["mathomp4", "kgerheiser", "climbfuji", "edwardhartnett", "Hang-Lei-NOAA"]

    version("develop", branch="develop")
    version("main", branch="main")

    version("2.26.0", sha256="4ef9a1eeffc0521bd6fb4ea5ab261e07d3b5a46f0a6c43673ee169bf0d624bb8")
    version("2.25.0", sha256="f3ce71004f4274cedee28852cc105e0bf51a86cafc4d5f5af9de6492c4be9402")
    version("2.24.0", sha256="cd15ffd6897c18e64267e5fa86523402eb48cbf638ad5f3b4b5b0ff8939d1936")
    version("2.23.1", sha256="563f3e9f33adae298835e7de7a4a29452a2a584d191248c59494c49d3ee80d24")
    version("2.23.0", sha256="ae25ec63d0f288599c668f35fdbccc76abadbfc6d48f95b6eb4e7a2c0c69f241")
    version("2.22.0", sha256="3356b8d29813431d272c5464e265f3fe3ce1ac7f49ae6d41da34fe4b82aa691a")
    version("2.12.3", sha256="e849eff291939509e74830f393cb2670c2cc96f6160d8060dbeb1742639c7d41")
    version("2.11.0", sha256="76351e026c17e2044b89085db639e05ba0e7439a174d14181e01874f0f93db44")
    version("2.8.1", sha256="a7657d4c52a66c3a6663e436d2c2dd4dbb81addd747e1ace68f59843665eb739")
    version("2.8.0", sha256="6da60a21ab77ecebc80575f25b756c398ef48f635ab0b9c96932a1d4ebd8b4a0")
    version("2.7.3", sha256="e8cdc0816471bb4c42673c2fa66d9d749f5a18944cd31580a2d6fd6d961ba163")
    version("2.7.2", sha256="8f123352c665c434a18ff87304a71a61fb3342919adcccfea2a40729992d9f93")
    version("2.7.1", sha256="8239fdbebd2caa47a232c24927f7a91196704e35c8b7909e1bbbefccf0647ea6")

    # Versions later than 3.14 remove FindESMF.cmake
    # from ESMA_CMake. This works with mapl@2.22.0:
    resource(
        name="esma_cmake",
        git="https://github.com/GEOS-ESM/ESMA_cmake.git",
        tag="v3.17.0",
        when="@2.22.0:",
    )
    resource(
        name="esma_cmake",
        git="https://github.com/GEOS-ESM/ESMA_cmake.git",
        tag="v3.13.0",
        when="@:2.12.3",
    )

    # Patch to configure Apple M1 chip in x86_64 Rosetta 2 emulator mode
    # Needed for versions earlier than 3.14 of ESMA_cmake only.
    patch("esma_cmake_apple_m1_rosetta.patch", when="@:2.12.3")

    # Patch to add missing NetCDF C target in various CMakeLists.txt
    patch("mapl-2.12.3-netcdf-c.patch", when="@:2.12.3")

    # Patch to add missing MPI Fortran target to top-level CMakeLists.txt
    patch("mapl-2.12.3-mpi-fortran.patch", when="@:2.12.3")

    variant("flap", default=False, description="Build with FLAP support")
    variant("pflogger", default=False, description="Build with pFlogger support")
    variant("shared", default=True, description="Build as shared library")
    variant("debug", default=False, description="Make a debuggable version of the library")
    variant("extdata2g", default=False, description="Use ExtData2G")
    variant("pfunit", default=False, description="Build with pFUnit support")

    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release", "Aggressive")
    )

    depends_on("cmake@3.17:")
    depends_on("mpi")
    depends_on("hdf5")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("esmf@8.3:", when="@2.22:")
    depends_on("esmf", when="@:2.12.99")
    depends_on("esmf~debug", when="~debug")
    depends_on("esmf+debug", when="+debug")
    
    depends_on("gftl@1.5.5:")
    depends_on("gftl-shared@1.3.1:")

    # There was an interface change in yaFyaml, so we need to control versions
    # MAPL 2.22 and older uses older version, MAPL 2.23+ and higher uses newer
    depends_on("yafyaml@1.0-beta5", when="@:2.22+extdata2g")
    depends_on("yafyaml@1.0.4:", when="@2.23:+extdata2g")

    # pFlogger depends on yaFyaml in the same way. MAPL 2.22 and below uses old
    # yaFyaml so we need to use old pFlogger, but MAPL 2.23+ uses new yaFyaml
    depends_on("pflogger@:1.6", when="@:2.22+pflogger")
    depends_on("pflogger@1.9.1:", when="@2.23:+pflogger")        

    depends_on("pfunit@4.2:", when="+pfunit")
    depends_on("flap", when="+flap")

    
    depends_on("ecbuild")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_WITH_FLAP", "flap"),
            self.define_from_variant("BUILD_WITH_PFLOGGER", "pflogger"),
            self.define_from_variant("BUILD_SHARED_MAPL", "shared"),
            self.define_from_variant("USE_EXTDATA2G", "extdata2g"),
            "-DCMAKE_C_COMPILER=%s" % self.spec["mpi"].mpicc,
            "-DCMAKE_CXX_COMPILER=%s" % self.spec["mpi"].mpicxx,
            "-DCMAKE_Fortran_COMPILER=%s" % self.spec["mpi"].mpifc,
        ]

        if self.spec.satisfies("@2.22.0:"):
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["esmf"].prefix.cmake))

        # Compatibility flags for gfortran
        fflags = []
        if self.compiler.name in ["gcc", "clang", "apple-clang"]:
            fflags.append("-ffree-line-length-none")
            gfortran_major_ver = int(
                spack.compiler.get_compiler_version_output(self.compiler.fc, "-dumpversion").split(
                    "."
                )[0]
            )
            if gfortran_major_ver >= 10:
                fflags.append("-fallow-invalid-boz")
                fflags.append("-fallow-argument-mismatch")
        if fflags:
            args.append(self.define("CMAKE_Fortran_FLAGS", " ".join(fflags)))

        return args
