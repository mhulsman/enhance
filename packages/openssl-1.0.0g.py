from package import *

class openssl(MakePackage):
    fetch="http://www.openssl.org/source/openssl-%(version)s.tar.gz"
    
    config="./config shared --prefix=%(prefix)s"

    build = "make -j1"
