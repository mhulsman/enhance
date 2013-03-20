from package import *;

class rmblast(MakePackage):
    dependencies=['ncbi_blast']
    fetch="ftp://ftp.ncbi.nlm.nih.gov/blast/executables/rmblast/2.2.27/rmblast-2.2.27-src.tar.gz"
    workdir="rmblast-2.2.27-src/c++/"
    config="./configure --with-mt --prefix=%(prefix)s --without-debug"
