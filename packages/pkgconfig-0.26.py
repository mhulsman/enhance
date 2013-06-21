from package import *

class pkgconfig(MakePackage):
    fetch="http://pkgconfig.freedesktop.org/releases/pkg-config-0.26.tar.gz"
    config="./configure --prefix=%(prefix)s --with-internal-glib"
