from package import *

class bwa(MakePackage):

    fetch="https://downloads.sourceforge.net/project/bio-bwa/bwa-0.7.3a.tar.bz2?r=https://sourceforge.net/Fprojects/Fbio-bwa/Ffiles/F&ts=1363796390&use_mirror=netcologne"
    def Config(self) :
        pass

    install= """
        cp bwa %(prefix)s/bin/
    """
