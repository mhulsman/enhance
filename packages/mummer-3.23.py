from package import *

class mummer(MakePackage):
    fetch="http://downloads.sourceforge.net/project/mummer/mummer/3.23/MUMmer3.23.tar.gz"

    config="make check"
    build="""
    mkdir -p %(prefix)s/opt/Mummer3.23
    cp -R * %(prefix)s/opt/Mummer3.23
    cd %(prefix)s/opt/Mummer3.23
    make install
    """
    install="""
    cd %(prefix)s/opt/Mummer3.23
    ln -f -s ../opt/Mummer3.23/mummer ../opt/Mummer3.23/annotate ../opt/Mummer3.23/combineMUMs ../opt/Mummer3.23/delta-filter ../opt/Mummer3.23/gaps ../opt/Mummer3.23/mgaps %(prefix)s/bin/
    ln -f -s ../opt/Mummer3.23/repeat-match ../opt/Mummer3.23/show-aligns ../opt/Mummer3.23/show-coords ../opt/Mummer3.23/show-tiling ../opt/Mummer3.23/show-snps ../opt/Mummer3.23/show-diff %(prefix)s/bin/
    ln -f -s ../opt/Mummer3.23/exact-tandems  ../opt/Mummer3.23/mapview ../opt/Mummer3.23/mummerplot ../opt/Mummer3.23/nucmer ../opt/Mummer3.23/promer ../opt/Mummer3.23/run-mummer1 ../opt/Mummer3.23/run-mummer3 ../opt/Mummer3.23/nucmer2xfig ../opt/Mummer3.23/dnadiff %(prefix)s/bin/
    """
