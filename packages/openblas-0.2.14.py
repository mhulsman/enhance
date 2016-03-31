from package import *
from tools import *

class openblas(MakePackage):
    dependencies=["gcc", "binutils"]

    fetch="http://github.com/xianyi/OpenBLAS/archive/v0.2.14.tar.gz"
    workdir="OpenBLAS-0.2.14"

    config=""

    build = """
        make all PREFIX="%(prefix)s" USE_OPENMP=0 DYNAMIC_ARCH=1 NUM_THREADS=56
        """
    
    install = """
        make install PREFIX="%(prefix)s"
        """

