from package import *;

class ncbi_blast(MakePackage):
    depenencies=['Archive']
    fetch='ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.27/ncbi-blast-2.2.27+-src.tar.gz'
    workdir="ncbi-blast-2.2.27+-src/c++/"
    config="./configure --with-mt --prefix=%(prefix)s --without-debug"
