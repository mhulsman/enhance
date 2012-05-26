from package import *


class pcre(MakePackage):
    fetch='ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.30.tar.gz'
    config="./configure --prefix=%(prefix)s --enable-utf"
