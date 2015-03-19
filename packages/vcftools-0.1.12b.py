from package import *

class vcftools(MakePackage):
    dependencies=['perl']

    fetch="http://downloads.sourceforge.net/project/vcftools/vcftools_0.1.12b.tar.gz"
    config=""

    build="""
        mkdir -p %(prefix)s/opt/vcftools
        cp -R * %(prefix)s/opt/vcftools
        cd %(prefix)s/opt/vcftools
        make
        """

    install="""
        cd %(prefix)s/opt/vcftools
        cp -rs %(prefix)s/opt/vcftools/bin/* %(prefix)s/bin/
        cat %(rootpath)s/paths | grep -v vcftools > temppath
        echo "export PERL5LIB=%(prefix)s/opt/vcftools/perl:$PERL5LIB" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
