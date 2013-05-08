from package import *

class star(MakePackage):
    fetch="http://rna-star.googlecode.com/files/STAR_2.3.0e.tgz"
    config=""
    build="""
        patch Genome.cpp < %(distpath)s/packages/star-2.3.0e.patch
        make
        """
    install="cp STAR %(prefix)s/bin/"


