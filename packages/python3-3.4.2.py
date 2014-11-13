from package import *

class python3(MakePackage):
    dependencies=["bzip2","ncurses", "sqlite","readline", "zlib", "openssl"]
    fetch="https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz"
    modify_environ = {'PYTHONPATH':'%(prefix)s/lib/python3.4/'}

    config="./configure --enable-shared --prefix=%(prefix)s"

    install="""
            make install
            mv %(prefix)s/bin/python3.4 %(prefix)s/bin/python3.4exec
            echo '#!/bin/bash\nPYTHONPATH=%(prefix)s/lib/python3.4/\npython3.4exec $@\n' > %(prefix)s/bin/python3.4
            chmod +x %(prefix)s/bin/python3.4
            """

