from package import *

class python(MakePackage):
    dependencies=["bzip2","ncurses", "sqlite","readline","zlib"]
    fetch="http://www.python.org/ftp/python/2.7/Python-2.7.tgz"

    config="./configure --enable-shared --prefix=%(prefix)s"

    install="""
            make install
            python setup.py install --prefix=%(prefix)s
            """

