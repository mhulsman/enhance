from package import *

class zeromq(MakePackage):
    dependencies=['e2fsprogs']
    fetch="http://download.zeromq.org/zeromq-4.0.3.tar.gz"
    
    config="./configure --prefix=%(prefix)s"
