from package import *

class bwa(MakePackage):

    fetch="http://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.5a.tar.bz2"
    
    def Config(self) :
        pass

    install= """
        cp bwa %(prefix)s/bin/
    """
