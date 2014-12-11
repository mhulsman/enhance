from package import *

class samtools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.1/samtools-1.1.tar.bz2"
    dependencies = ['zlib','ncurses']
    build="make"
    
    install="""
    make prefix=%(prefix)s install
    """
