# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NceplibsSigio(CMakePackage):
    """This library provides an Application Program Interface for
performing I/O on the sigma restart file of the global spectral
model. Functions include opening, reading, writing, and closing as
well as allocating and deallocating data buffers used in the
transfers. The I/O performed here is sequential. The transfers are
limited to header records or data records.

This is part of the NCEPLIBS project.

    """

    homepage = "https://github.com/NOAA-EMC/NCEPLIBS-sigio"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-sigio/archive/refs/tags/v2.3.2.tar.gz"

    maintainers = ['edwardhartnett', 'kgerheiser', 'Hang-Lei-NOAA']

    version('2.3.2', sha256='333f3cf3a97f97103cbafcafc2ad89b24faa55b1332a98adc1637855e8a5b613')

