from package import *
class gmp(MakePackage):
    fetch='https://gmplib.org/download/gmp/gmp-6.0.0a.tar.bz2'
    workdir="gmp-6.0.0"
    config="./configure --build=x86_64-unknown-linux-gnu --prefix=%(prefix)s --enable-cxx"

