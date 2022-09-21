# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mepo(Package):
    """
    Tool to manage (m)ultiple git r(epo)sitories
    """

    homepage = "https://github.com/GEOS-ESM/mepo/"
    url = "https://github.com/GEOS-ESM/mepo/archive/refs/tags/v1.45.0.tar.gz"

    maintainers = ['kgerheiser']

    version('1.45.0', sha256='276ca8eb12f7bd9e5117a7f7a2596147456b7db05dbe93f5cd778da0b2ed80de')

    depends_on('python@3.9:', type=('run'))
    depends_on('py-pyyaml', type=('run'))

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
