from package import *

class fasta(Package):
    fetch="http://faculty.virginia.edu/wrpearson/fasta/fasta36/fasta-36.3.7a.tar.gz"

    config=""

    build="""
        mkdir -p %(prefix)s/opt/fasta
        cp -R * %(prefix)s/opt/fasta
        cd %(prefix)s/opt/fasta
        cd src
        make -f ../make/Makefile.linux64_sse2 all
        """

    install="""
        cd %(prefix)s/opt/fasta
        ln -f -s %(prefix)s/opt/fasta/bin/*  %(prefix)s/bin/
    """        



