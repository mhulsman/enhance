from package import *

class zeromq(MakePackage):
    dependencies=['e2fsprogs']
    fetch="http://download.zeromq.org/zeromq-2.1.11.tar.gz"
    
    config="./configure --prefix=%(prefix)s"
