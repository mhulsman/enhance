from package import *

class pkgconfig(MakePackage):
    dependencies=['glib']
    fetch="http://pkgconfig.freedesktop.org/releases/pkg-config-0.26.tar.gz"
