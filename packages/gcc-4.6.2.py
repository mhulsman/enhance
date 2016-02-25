from package import *
class gcc(MakePackage):
    dependencies=['ppl','cloogppl==0.15.11','mpc','mpfr','gmp']
    modify_environ={'LIBRARY_PATH':''}

    fetch='ftp://ftp.nluug.nl/mirror/languages/gcc/releases/gcc-4.6.2/gcc-4.6.2.tar.gz'
    workdir="gcc-4.6.2/build"
    config="../configure --prefix=%(prefix)s --with-ppl=%(prefix)s --with-cloog=%(prefix)s -with-mpc=%(prefix)s --with-mpfr=%(prefix)s -with-gmp=%(prefix)s --disable-multilib"
    
