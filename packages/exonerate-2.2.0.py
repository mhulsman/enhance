from package import *

class exonerate(MakePackage):
    dependencies=['glib']
    fetch="http://www.ebi.ac.uk/~guy/exonerate/exonerate-2.2.0.tar.gz"
    config="CFLAGS=\"-Wno-ununsed\" ./configure --prefix=%(prefix)s --disable-paranoia --disable-gprof --disable-largefile"
    build="make -j1"
