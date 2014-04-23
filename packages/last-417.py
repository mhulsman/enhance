from package import *

class last(MakePackage):
    dependencies=['gcc']
    fetch="http://last.cbrc.jp/last-417.zip"
    config=""
    install="make install prefix=%(prefix)s"
