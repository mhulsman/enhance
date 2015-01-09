from package import *

class samtools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.1/samtools-1.1.tar.bz2"
    dependencies = ['zlib','ncurses']
    build="make"

    config = """
    patch -p0 < %(distpath)s/packages/samtools_1.1_stats.patch
    """

    install="""
    make prefix=%(prefix)s install
    """
