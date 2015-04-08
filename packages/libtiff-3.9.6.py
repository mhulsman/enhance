from package import *

class libtiff(MakePackage):
    fetch="ftp://ftp.remotesensing.org/pub/libtiff/tiff-3.9.6.zip"
    workdir="tiff-3.9.6"
    config="./configure --prefix=%(prefix)s"
