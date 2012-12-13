from package import *

class express(MakePackage):
    dependencies=['bamtools','cmake','boost']
    fetch="http://bio.math.berkeley.edu/eXpress/downloads/express-1.2.2/express-1.2.2-src.tgz"
    
    config="""
        ln -s %(prefix)s bamtools
        mkdir build
        cd build
        BOOST_ROOT=%(prefix)s cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s
    """

    build="""
        patch src/main.h < %(distpath)s/packages/express-1.2.2.patch
        cd build
        make
        """

    install="""
        cd build
        make install
    """    
