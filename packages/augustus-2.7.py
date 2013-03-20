from package import *

class augustus(MakePackage):
    dependencies=[]
    fetch='http://bioinf.uni-greifswald.de/augustus/binaries/augustus.2.7.tar.gz'
    config=""

    build="""
        mkdir -p %(prefix)s/opt/augustus
        cp -R * %(prefix)s/opt/augustus
        cd %(prefix)s/opt/augustus
        cd src
        make
        """

    install="""
        cd %(prefix)s/opt/augustus
        cp -rs %(prefix)s/opt/augustus/bin/* %(prefix)s/bin/
        cat %(rootpath)s/paths | grep -v AUGUSTUS_CONFIG_PATH > temppath
        echo "export AUGUSTUS_CONFIG_PATH=%(prefix)s/opt/augustus/config" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
