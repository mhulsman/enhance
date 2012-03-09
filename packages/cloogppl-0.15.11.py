from package import *
class cloogppl(MakePackage):
    dependencies=['ppl','gmp']
    fetch='ftp://gcc.gnu.org/pub/gcc/infrastructure/cloog-ppl-0.15.11.tar.gz'
    config="./configure --prefix=%(prefix)s --with-ppl=%(prefix)s --with-gmp=%(prefix)s"

