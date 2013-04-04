from package import *
class gcc(MakePackage):
    dependencies=['cloog==0.18.0','mpc','mpfr','gmp']
    modify_environ={'LIBRARY_PATH':''}

    fetch='ftp://ftp.nluug.nl/mirror/languages/gcc/releases/gcc-%(version)s/gcc-%(version)s.tar.gz'
    workdir="gcc-%(version)s/build"
    config="../configure --prefix=%(prefix)s --with-ppl=%(prefix)s --with-cloog=%(prefix)s -with-mpc=%(prefix)s --with-mpfr=%(prefix)s -with-gmp=%(prefix)s --disable-multilib"
    
