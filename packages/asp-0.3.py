from package import *

class asp(MakePackage):
  
    dependencies=['shogun','numpy']
    fetch="http://ftp.raetschlab.org/software/asp/asp_0.3.tar.bz2"

    workdir="asp"
    config=""
    build="""
        mkdir -p %(prefix)s/opt/asp
        cp -R * %(prefix)s/opt/asp
        """

    install="""
        cd %(prefix)s/opt/asp
        ln -f -s ../opt/asp/asp %(prefix)s/bin/
    """ 

