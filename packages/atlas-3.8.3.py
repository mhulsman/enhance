from package import *

class atlas(MakePackage):
    dependencies=["lapack"]

    fetch="http://downloads.sourceforge.net/project/math-atlas/Stable/%(version)s/atlas%(version)s.tar.gz"

    workdir = "ATLAS/build_dir"

    config="../configure -Fa alg -fPIC --with-netlib-lapack=%(prefix)s/lib/lapack_LINUX.a --prefix=%(prefix)s"

    build = "make -j1"
