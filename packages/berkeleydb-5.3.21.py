from package import *

class berkeleydb(MakePackage):
    fetch="http://download.oracle.com/berkeley-db/db-5.3.21.tar.gz"
    config="""
        cd build_unix
        ../dist/configure --prefix=%(prefix)s --enable-sql
        """
    build="""
        cd build_unix
        make
        """
    install="""
        cd build_unix
        make install
        """
