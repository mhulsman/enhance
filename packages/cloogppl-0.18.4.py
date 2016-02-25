from package import *
class cloogppl(MakePackage):
    dependencies=['ppl','gmp']
    fetch='http://www.bastoul.net/cloog/pages/download/count.php3?url=./cloog-0.18.4.tar.gz'
    config="./configure --prefix=%(prefix)s --with-ppl=%(prefix)s --with-gmp=%(prefix)s"

