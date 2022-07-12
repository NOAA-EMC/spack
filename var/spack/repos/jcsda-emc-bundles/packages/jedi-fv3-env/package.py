# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class JediFv3Env(BundlePackage):
    """Development environment for fv3-bundle"""

    homepage = "https://github.com/JCSDA/fv3-bundle"
    git      = "https://github.com/JCSDA/fv3-bundle.git"

    maintainers = ['climbfuji', 'rhoneyager']

    version('1.0.0')

    depends_on('base-env',          type='run')
    depends_on('fms@release-jcsda', type='run')
    depends_on('jedi-base-env',     type='run')

    # There is no need for install() since there is no code.
