from package import *

class shogun(MakePackage):
  
  dependencies=['numpy', 'atlas','lapack','R','perl','eigen','swig']
  fetch="ftp://shogun-toolbox.org/shogun/releases/2.1/sources/shogun-2.1.0.tar.bz2"

  workdir="shogun-2.1.0/src"
  config="""
        PERL_MM_USE_DEFAULT=1 INC="-I%(prefix)s/include" cpan PDL
        ./configure --prefix=%(prefix)s --interfaces=cmdline_static,python_modular,r_modular --disable-lapack
        """

  
