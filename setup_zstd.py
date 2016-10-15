# Copyright (c) 2016-present, Gregory Szorc
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license. See the LICENSE file for details.

import os
from distutils.extension import Extension


zstd_sources = ['zstd/%s' % p for p in (
    'common/entropy_common.c',
    'common/fse_decompress.c',
    'common/xxhash.c',
    'common/zstd_common.c',
    'compress/fse_compress.c',
    'compress/huf_compress.c',
    'compress/zbuff_compress.c',
    'compress/zstd_compress.c',
    'decompress/huf_decompress.c',
    'decompress/zbuff_decompress.c',
    'decompress/zstd_decompress.c',
    'dictBuilder/divsufsort.c',
    'dictBuilder/zdict.c',
)]


zstd_includes = [
    'zstd',
    'zstd/common',
    'zstd/compress',
    'zstd/decompress',
    'zstd/dictBuilder',
]


def get_c_extension(name='zstd'):
    """Obtain a distutils.extension.Extension for the C extension."""
    root = os.path.abspath(os.path.dirname(__file__))

    sources = [os.path.join(root, p) for p in zstd_sources + ['zstd.c']]
    include_dirs = [os.path.join(root, d) for d in zstd_includes]

    # TODO compile with optimizations.
    return Extension(name, sources,
                     include_dirs=include_dirs)