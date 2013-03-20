from package import *

class snap(MakePackage):
    fetch = 'http://korflab.ucdavis.edu/Software/snap-2013-02-16.tar.gz'
   
    workdir='snap'

    config=""

    build="""
        mkdir -p %(prefix)s/opt/snap
        cp -R * %(prefix)s/opt/snap
        cd %(prefix)s/opt/snap
        make
        """

    install="""
        cd %(prefix)s/opt/snap
        cat %(rootpath)s/paths | grep -v ZOE > temppath
        echo "export ZOE=%(prefix)s/opt/snap/Zoe" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
