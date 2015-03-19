from package import *

class samtools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.2/samtools-1.2.tar.bz2"
    dependencies = ['zlib','ncurses']
    build="make"

    #config = """
    #patch -p0 < %(distpath)s/packages/samtools_1.2_stats.patch
    #"""
    config =""

    install="""
    make prefix=%(prefix)s install
    """
