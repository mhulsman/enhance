from package import *

class tabix(MakePackage):
    dependencies=[]

    fetch="http://downloads.sourceforge.net/project/samtools/tabix/tabix-0.2.6.tar.bz2"

    config=""

    build="""
        mkdir -p %(prefix)s/opt/tabix
        cp -R * %(prefix)s/opt/tabix
        cd %(prefix)s/opt/tabix
        make
        """

    install="""
        cd %(prefix)s/opt/tabix
        cp -rs %(prefix)s/opt/tabix/bgzip %(prefix)s/bin/
        cp -rs %(prefix)s/opt/tabix/tabix %(prefix)s/bin/
    """ 
