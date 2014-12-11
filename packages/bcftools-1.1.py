from package import *

class bcftools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.1/bcftools-1.1.tar.bz2"
    dependencies = ['zlib']
    build="make"
    
    install="make prefix=%(prefix)s install"
