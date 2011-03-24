from package import *

class atlas(MakePackage):
    dependencies=["lapack"]

    fetch="http://downloads.sourceforge.net/project/math-atlas/Stable/3.8.3/atlas%(version)s.tar.gz"

    workdir = "ATLAS/build_dir"

    config="../configure -Fa alg -fPIC --with-netlib-lapack=%(prefix)s/lib/lapack_LINUX.a --prefix=%(prefix)s"


