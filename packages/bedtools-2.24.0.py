from package import *

class bedtools(MakePackage):
    fetch="https://github.com/arq5x/bedtools2/releases/download/v2.24.0/bedtools-2.24.0.tar.gz"
   
    workdir="bedtools2"
    config=""
    build="make"
    install="""
    cp -R ./bin/* %(prefix)s/bin
    """

    
    
