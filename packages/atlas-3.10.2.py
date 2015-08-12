from package import *
from tools import *

class atlas(MakePackage):
    dependencies=["gcc"]
    def fetch(self):
        self.package_file = download(self.fillVars("http://downloads.sourceforge.net/project/math-atlas/Stable/%(version)s/atlas%(version)s.tar.bz2"))
        self.lapack_file = download("http://www.netlib.org/lapack/lapack-3.5.0.tgz")

    workdir = "ATLAS/build_dir"

    config="""../configure -C acg %(prefix)s/bin/gcc -C if %(prefix)s/bin/gfortran -b 64 -t 8 -Fa alg -fPIC -D c -DWALL --force-tids="8 0 1 2 3 4 5 6 7" --with-netlib-lapack-tarfile=%(src)s/lapack-3.5.0.tgz --prefix=%(prefix)s"""

    build = """
        ulimit -s 65000 
        make -j1
        """


