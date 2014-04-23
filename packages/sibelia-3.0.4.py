from package import *

class sibelia(MakePackage):
    dependencies=['gcc','cmake']
    fetch="http://downloads.sourceforge.net/project/sibelia-bio/3.0.4/Sibelia-3.0.4-Source.tar.gz"

    build_reldir = "build"
    config = "cmake ../src -DCMAKE_INSTALL_PREFIX=%(prefix)s"

