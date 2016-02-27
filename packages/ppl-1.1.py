from package import *
class ppl(MakePackage):
    dependencies=['gmp']
    fetch='http://bugseng.com/products/ppl/download/ftp/releases/1.1/ppl-1.1.tar.gz'
    config="./configure --prefix=%(prefix)s"

