from package import *

class tophat(MakePackage):
    dependencies=['boost','samtools','bowtie2']
    fetch="http://tophat.cbcb.umd.edu/downloads/tophat-2.0.6.tar.gz"
    config="./configure --prefix=%(prefix)s --with-boost=%(prefix)s"
    build="""
        cd src
        make libtophat.a
        cd ..
        make
        """


