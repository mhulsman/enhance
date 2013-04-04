from package import *

class cufflinks(MakePackage):
    dependencies=['eigen','boost','samtools']
    fetch="http://cufflinks.cbcb.umd.edu/downloads/cufflinks-2.0.2.tar.gz"
    config="./configure --prefix=%(prefix)s --with-boost=%(prefix)s"
    build="""
    patch -R src/common.h < %(distpath)s/packages/cufflinks-2.0.2.patch
    patch src/lemon/bits/base_extender.h < %(distpath)s/packages/cufflinks-2.0.2-gcc4.8.patch
    make
    """


