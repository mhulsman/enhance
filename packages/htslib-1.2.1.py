from package import *

class htslib(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.2/htslib-1.2.1.tar.bz2"
    dependencies = ['zlib']
    build="make"
    
    install="make prefix=%(prefix)s install"
