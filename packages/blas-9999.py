from package import *

class blas(MakePackage):
    fetch="http://www.netlib.org/blas/blas.tgz"
    workdir="BLAS"
    config=""
    install="cp %(srcpath)s/BLAS/blas_LINUX.a %(prefix)s/lib/libblas.a"


