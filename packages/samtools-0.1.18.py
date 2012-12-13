from package import *

class samtools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/0.1.18/samtools-0.1.18.tar.bz2"
    dependencies = ['zlib','ncurses']
    build="""
    make
    make razip
    """
    
    install="""
    cp samtools bcftools/bcftools %(prefix)s/bin/
    cp misc/seqtk misc/wgsim misc/maq2sam-* misc/md5fa misc/md5sum-lite %(prefix)s/bin/
    cp misc/*.pl %(prefix)s/bin/
    cp libbam.a %(prefix)s/lib/
    mkdir %(prefix)s/include/bam
    cp *.h %(prefix)s/include/bam/
    """
