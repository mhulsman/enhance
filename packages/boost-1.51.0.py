from package import *

class boost(Package):
    fetch="http://downloads.sourceforge.net/project/boost/boost/1.51.0/boost_1_51_0.tar.gz"

    config="./bootstrap.sh --prefix=%(prefix)s"

    install = "./b2 install"
