from package import *

class autoconf(MakePackage):
    dependencies = ['m4','pkgconfig','libtool','perl']
    fetch="http://ftp.gnu.org/gnu/autoconf/autoconf-2.68.tar.gz"

    install = """
                make install
                echo "export ACLOCAL_PATH=%(prefix)s/share/aclocal" >> %(prefix)s/../paths
              """                

