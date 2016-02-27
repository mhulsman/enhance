from package import *

class last(MakePackage):
    dependencies=['gcc==4.6.2']
    fetch="http://last.cbrc.jp/last-417.zip"
    config=""
    install="make install prefix=%(prefix)s"
