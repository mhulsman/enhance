from package import *
class gmp(MakePackage):
    fetch='ftp://ftp.gmplib.org/pub/gmp-5.0.2/gmp-5.0.2.tar.bz2'
    config="./configure --build=x86_64-unknown-linux-gnu --prefix=%(prefix)s --enable-cxx"

