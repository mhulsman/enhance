from package import *

class bzip2(Package):
    fetch="http://www.bzip.org/%(version)s/bzip2-%(version)s.tar.gz"

    build="make -f Makefile-libbz2_so"

    install="make install PREFIX=%(prefix)s"

    
    
