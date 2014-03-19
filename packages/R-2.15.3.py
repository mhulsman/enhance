from package import *

class R(MakePackage):
    dependencies = ["tcl","tk",'xorg']
    fetch="http://cran.xl-mirror.nl/src/base/R-2/R-2.15.3.tar.gz"
    config = "./configure --prefix=%(prefix)s --with-tcl-config=%(prefix)s/lib64/tclConfig.sh --with-tk-config=%(prefix)s/lib64/tkConfig.sh --enable-R-shlib"

