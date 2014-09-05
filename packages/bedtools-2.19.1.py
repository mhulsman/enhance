from package import *

class bedtools(MakePackage):
    fetch="https://github.com/arq5x/bedtools2/archive/v2.19.1.tar.gz"
   
    workdir="bedtools2-2.19.1"
    config=""
    build="make"
    install="""
    cp -R ./bin/* %(prefix)s/bin
    """

    
    
