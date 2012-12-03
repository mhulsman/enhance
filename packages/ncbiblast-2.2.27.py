from package import *;

class ncbiblast(MakePackage):
    dependencies=['gcc']
    modify_environ={'LIBRARY_PATH':''}

    fetch='ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.27/ncbi-blast-2.2.27+-src.tar.gz"
    workdir="ncbi-blast-2.2.27+-src/c++/"
    config="../configure --prefix=%(prefix)s --with-ppl=%(prefix)s"
