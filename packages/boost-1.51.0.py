from package import *

class boost(Package):
    fetch="http://downloads.sourceforge.net/project/boost/boost/1.51.0/boost_1_51_0.tar.gz"

    config="""
            cd ./libs/context/src/asm/
            cp %(distpath)s/packages/boost_ppc64_1.51.patch .
            patch -p0 < boost_ppc64_1.51.patch
            cd ../../../../
            ./bootstrap.sh --prefix=%(prefix)s
            """

    install = "./b2 install"
