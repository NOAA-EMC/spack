# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gptl
#
# You can edit this file again by typing:
#
#     spack edit gptl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gptl(AutotoolsPackage):
    """
    GPTL is a library to instrument C, C++, and Fortran codes for
    performance analysis and profiling.

    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://jmrosinski.github.io/GPTL/"
    url      = "https://github.com/jmrosinski/GPTL/releases/download/v8.0.3/gptl-8.0.3.tar.gz"

    version('8.0.3', sha256='334979c6fe78d4ed1b491ec57fb61df7a910c58fd39a3658d03ad89f077a4db6')
    version('8.0.2', sha256='011f153084ebfb52b6bf8f190835d4bae6f6b5c0ad320331356aa47a547bf2b4')

    variant('pmpi', default=False)
    variant('papi', default=False)
    variant('nestedomp', default=False)
    variant('disable-unwind', default=False)

    depends_on('mpi')

    def configure_args(self):
        args = []

        if '+pmpi' in self.spec:
            args.append('--enable-pmpi')
            args.append('CC={}'.format(self.spec['mpi'].mpicc))

        if '+papi' in self.spec:
            args.append('--enable-papi')

        if '+nestedomp' in self.spec:
            args.append('--enable-nestedomp')

        if '+disable-unwind' in self.spec:
            args.append('--disable-libunwind')

        return args
