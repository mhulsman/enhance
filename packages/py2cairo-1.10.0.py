from package import *

class py2cairo(Package):
    dependencies = ["cairo"]
    fetch="http://cairographics.org/releases/py2cairo-1.10.0.tar.bz2"

    install = '''
    ./waf configure --prefix=%(prefix)s
    ./waf build
    ./waf install
    '''
