from package import *

class samstat(Package):
    fetch="http://downloads.sourceforge.net/project/samstat/samstat.tgz"

    build="""
    cd src
    make
    """

    install="""
    cd src
    cp samstat %(prefix)s/bin/
    """

    
    
