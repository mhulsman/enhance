from package import *

class fontconfig(MakePackage):
    dependencies = ['libxml','freetype']
    fetch="http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.8.0.tar.gz"
