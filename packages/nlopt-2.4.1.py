from package import *

class nlopt(MakePackage):
    config = './configure --prefix=%(prefix)s --enable-shared --without-octave --without-matlab'
    fetch="http://ab-initio.mit.edu/nlopt/nlopt-2.4.1.tar.gz"

    
    
