from package import *

class cblas(MakePackage):
    dependencies=['blas']
    fetch="http://www.netlib.org/blas/blast-forum/cblas.tgz"
    workdir="CBLAS"
    config="""
        rm Makefile.in
        cat Makefile.LINUX | sed s#libblas.a#%(prefix)s/lib/libblas.a# > Makefile.in
        """
    build="make"        
    install="""
            cp %(srcpath)s/CBLAS/lib/cblas_LINUX.a %(prefix)s/lib/libcblas.a
            cp -R %(srcpath)s/CBLAS/include %(prefix)s/include/CBLAS
            cp -R %(srcpath)s/CBLAS/include %(prefix)s/include/
            """


