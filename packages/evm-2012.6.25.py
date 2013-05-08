from package import *

class evm(Package):
    dependencies=['perl']
    fetch = 'http://downloads.sourceforge.net/project/evidencemodeler/evidencemodeler/EVM_r2012-06-25.tgz'
    
    config=""

    build="""
        mkdir -p %(prefix)s/opt/evm
        cp -R * %(prefix)s/opt/evm
        cd %(prefix)s/opt/evm
        """

    install="""
        cat %(rootpath)s/paths | grep -v EVMHOME > temppath
        echo "export EVMHOME=%(prefix)s/opt/evm" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
