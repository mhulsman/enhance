from package import *

class python(MakePackage):
    dependencies=["bzip2","ncurses", "sqlite","readline", "zlib", "openssl"]
    fetch="https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz"

    config="./configure --enable-shared --prefix=%(prefix)s"

    install="""
            make install
            python setup.py install --prefix=%(prefix)s
            """

