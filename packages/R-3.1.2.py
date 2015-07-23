from package import *

class R(MakePackage):
    dependencies = ["tcl","tk",'xorg']
    fetch="http://cran.xl-mirror.nl/src/base/R-3/R-3.1.2.tar.gz"
    config = "./configure --prefix=%(prefix)s --with-tcl-config=%(prefix)s/lib64/tclConfig.sh --with-tk-config=%(prefix)s/lib64/tkConfig.sh --enable-R-shlib"

