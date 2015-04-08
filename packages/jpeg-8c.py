from package import *

class jpeg(MakePackage):
    fetch="http://www.ijg.org/files/jpegsrc.v8c.tar.gz"
    workdir="jpeg-8c"
    config="./configure --enable-shared --prefix=%(prefix)s"
