from package import *

class glibc(MakePackage):
    fetch="http://ftp.gnu.org/gnu/glibc/glibc-2.12.1.tar.gz"

    config="""
            mkdir build
            cd build
            ../configure --prefix=%(prefix)s
           """
