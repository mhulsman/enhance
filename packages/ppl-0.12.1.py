from package import *
class ppl(MakePackage):
    dependencies=['gmp']
    fetch='ftp://ftp.cs.unipr.it/pub/ppl/releases/0.12.1/ppl-0.12.1.tar.gz'
    config="./configure --prefix=%(prefix)s --disable-documentation"

