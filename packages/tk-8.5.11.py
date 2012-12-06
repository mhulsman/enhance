from package import *

class tk(MakePackage):
    dependencies = ["tcl"]
    fetch="http://prdownloads.sourceforge.net/tcl/tk8.5.11-src.tar.gz"
    workdir="tk8.5.11/unix"


