# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Madis(MakefilePackage):
    """MADIS: The Meteorological Assimilation Data Ingest System (MADIS) is
    dedicated toward making value-added data available from the National
    Oceanic and Atmospheric Administration's (NOAA) Earth System Research
    Laboratory (ESRL) Global Systems Division (GSD) (formerly the Forecast
    Systems Laboratory (FSL)) for the purpose of improving weather
    forecasting, by providing support for data assimilation, numerical
    weather prediction, and other hydrometeorological applications.
    """

    homepage = "https://madis-data.ncep.noaa.gov/"
    url = "https://madis-data.ncep.noaa.gov/source/madis-4.3.tar.gz"

    maintainers = ["AlexanderRichert-NOAA"]

    version("4.3", sha256="5d1ee9800c84e623dcf4271653aa66d17a744143e58354e70f8a0646cd6b246c")

    variant("pic", default=True, description="Build with PIC")
    variant("pnetcdf", default=False, description="Build with parallel NetCDF")

    depends_on("netcdf-fortran")
    depends_on("parallel-netcdf", when="+pnetcdf")

    def setup_build_environment(self, env):
        if self.spec.satisfies("+pic"):
            env.set("FFLAGS", "-fPIC")
            env.set("CFLAGS", "-fPIC")

        ldflags = []
        libs = []

        if self.spec.satisfies("+pnetcdf"):
            pnetcdf = self.spec["parallel-netcdf"]
            ldflags.append(pnetcdf.libs.ld_flags)
            libs.append(pnetcdf.libs.link_flags)

        nfconfig = which("nf-config")
        ldflags.append(nfconfig("--flibs", output=str).strip())
        netcdf_f = self.spec["netcdf-fortran"]
        env.set("NETCDF_INC", netcdf_f.prefix.include)

        env.set("NETCDF_LIB", " ".join(ldflags))
        env.set("LIBS", " ".join(libs))

    def build(self, spec, prefix):
        with working_dir("src"):
            make("-j1")

    def install(self, spec, prefix):
        with working_dir("src"):
            make("-j1")
        with working_dir(self.build_directory):
            copy_tree("bin", prefix.bin)
            copy_tree("doc", prefix.doc)
            copy_tree("include", prefix.include)
            copy_tree("lib", prefix.lib)
            copy_tree("src", prefix.src)
            copy_tree("static", prefix.static)

    def patch(self):
        filter_file("NETCDF_LIB=", "#NETCDF_LIB=", "src/makefile")
        filter_file("NETCDF_INC=", "#NETCDF_INC=", "src/makefile")
        filter_file("FC=", "#FC=", "src/makefile")
        filter_file("FFLAGS=", "#FFLAGS=", "src/makefile")
        filter_file("LDFLAGS=", "#LDFLAGS=", "src/makefile")
