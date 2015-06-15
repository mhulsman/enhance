from package import *

class python(MakePackage):
    dependencies=["bzip2","ncurses", "sqlite","readline", "zlib", "openssl"]
    fetch="http://www.python.org/ftp/python/2.7/Python-2.7.tgz"

    config="./configure --enable-shared --prefix=%(prefix)s"

    install="""
            make install
            python setup.py install --prefix=%(prefix)s
            echo '#!/bin/bash\nPYTHONPATH=%(prefix)s/lib/python2.7/\npython2.7 $@\n' > %(prefix)s/bin/python2
            chmod +x %(prefix)s/bin/python2
            """
