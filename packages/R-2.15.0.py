from package import *

class R(MakePackage):
    dependencies = ["tcl","tk"]
    fetch="http://cran.xl-mirror.nl/src/base/R-2/R-2.15.0.tar.gz"
    config = "./configure --prefix=%(prefix)s --with-tcl-config=%(prefix)s/lib64/tclConfig.sh --with-tk-config=%(prefix)s/lib64/tkConfig.sh"

