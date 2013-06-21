from package import *

class trinity(Package):
    dependencies=['perl']
    fetch = 'http://downloads.sourceforge.net/project/trinityrnaseq/trinityrnaseq_r2013-02-25.tgz'
    
    config=""

    build="""
        PERL_MM_USE_DEFAULT=1 cpan PerlIO::gzip
        mkdir -p %(prefix)s/opt/trinity
        cp -R * %(prefix)s/opt/trinity
        cd %(prefix)s/opt/trinity
        make
        """

    install="""
        cd %(prefix)s/opt/trinity
        ln -f -s ../opt/trinity/Trinity.pl %(prefix)s/bin/
        ln -f -s ../opt/trinity/util/normalize_by_kmer_coverage.pl %(prefix)s/bin/
    """ 
