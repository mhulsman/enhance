from package import *

class zeromq(MakePackage):
    dependencies=['e2fsprogs','sodium']
    fetch="http://download.zeromq.org/zeromq-4.1.4.tar.gz"
    
    config="./configure --prefix=%(prefix)s"
