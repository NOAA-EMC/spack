# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Fargparse(CMakePackage):
    """Command line argument parsing for Fortran"""

    homepage = "https://github.com/Goddard-Fortran-Ecosystem/fArgParse"
    url = "https://github.com/Goddard-Fortran-Ecosystem/fArgParse/archive/refs/tags/v1.1.2.tar.gz"
    git = "https://github.com/Goddard-Fortran-Ecosystem/fArgParse.git"

    maintainers = ["mathomp4", "tclune"]

    version("develop", branch="develop")
    version("main", branch="main")

    version("1.3.1", sha256="65d168696762b53f9a34fac8a82527fb602372f47be05018ebb382ec27b52c6c")
    version("1.3.0", sha256="08fde5fb1b739b69203ac336fe7b39915cfc7f52e068e564b9b6d905d79fc93d")
    version("1.2.0", sha256="4d14584d2bd5406267e3eacd35b50548dd9e408526465e89514690774217da70")
    version("1.1.2", sha256="89f63f181ccf183ca6212aee7ed7e39d510e3df938b0b16d487897ac9a61647f")

    depends_on("gftl-shared", type="build")
    depends_on("gftl", type="build")

    variant(
        "build_type", 
        default="Release",
        description="The build type to build",
        values=("Debug", "Release"),
    )
