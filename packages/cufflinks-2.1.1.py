from package import *

class cufflinks(MakePackage):
    dependencies=['eigen','boost','samtools']
    fetch="http://cufflinks.cbcb.umd.edu/downloads/cufflinks-2.1.1.tar.gz"
    config="./configure --prefix=%(prefix)s --with-boost=%(prefix)s"
    build="make"


