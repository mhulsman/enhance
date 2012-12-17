from package import *

class star(MakePackage):
    fetch="ftp://ftp2.cshl.edu/gingeraslab/tracks/STARrelease/2.2.0/STAR_2.2.0c.tgz"
    config=""
    build="""
        patch Makefile < %(distpath)s/packages/star-2.2.0c.patch
        make
        """
    install="cp STAR %(prefix)s/bin/"


