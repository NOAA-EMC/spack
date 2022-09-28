# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Geosgcm(CMakePackage):
    """
    GEOS Earth System Model GEOSgcm Fixture
    """

    homepage = "https://github.com/GEOS-ESM/GEOSgcm"
    git = "https://github.com/GEOS-ESM/GEOSgcm.git"

    maintainers = ["mathomp4", "tclune"]

    version("main", branch="main")
    version("10.23.0", tag="v10.23.0")

    variant("f2py", default=False, description="Build with f2py support")
    variant("extdata2g", default=True, description="Use ExtData2G")
    variant("geosdev", default=False, description="mepo develop GEOSgcm_GridComp, GEOSgcm_App, and GMAO_Shared")

    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release", "Aggressive"),
    )

    depends_on("mepo")
    depends_on("cmake@3.17:")
    depends_on("mpi")
    depends_on("ecbuild")

    # These are for mepo as well as MAPL AGC and stubber
    depends_on("python@3:")
    depends_on("py-pyyaml")
    depends_on("perl")

    # These are similarly the dependencies of MAPL. Not sure if we'll ever use MAPL as library
    depends_on("hdf5")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("esmf@8.3.0")
    depends_on("gftl@1.5.5:")
    depends_on("gftl-shared@1.3.1:")
    depends_on("yafyaml@1.0.4:", when="+extdata2g")
    depends_on("pflogger@1.9.1:")
    depends_on("flap@geos")

    # MAPL as library would be like:
    #depends_on("mapl@2.26:+flap+pflogger+extdata2g")

    # If we move to FMS as library, we'll need to add this:
    #depends_on("fms@2022.02:~gfs_phys+fpic~quad_precision+32bit+64bit constants=GEOS")

    # Before we run cmake, we need to run 'mepo clone' to get the full source
    @run_before("cmake")
    def mepo_clone(self):
        mepo = which("mepo")
        mepo("clone")
        # If the geosdev variant is set, we need to mepo develop GEOSgcm_GridComp, GEOSgcm_App, and GMAO_Shared
        if "+geosdev" in self.spec:
            mepo("develop", "GEOSgcm_GridComp", "GEOSgcm_App", "GMAO_Shared")

    def cmake_args(self):
        args = [
            self.define_from_variant("USE_F2PY", "f2py"),
            self.define_from_variant("USE_EXTDATA2G", "extdata2g"),
            self.define("CMAKE_MODULE_PATH", self.spec["esmf"].prefix.cmake),
            "-DCMAKE_C_COMPILER=%s" % self.spec["mpi"].mpicc,
            "-DCMAKE_CXX_COMPILER=%s" % self.spec["mpi"].mpicxx,
            "-DCMAKE_Fortran_COMPILER=%s" % self.spec["mpi"].mpifc,
        ]


        return args
