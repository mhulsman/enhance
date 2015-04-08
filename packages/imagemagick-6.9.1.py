from package import *

class imagemagick(MakePackage):
    fetch="http://www.imagemagick.org/download/ImageMagick.tar.gz"
    workdir="ImageMagick-6.9.1-0"
    config="./configure --prefix=%(prefix)s"
