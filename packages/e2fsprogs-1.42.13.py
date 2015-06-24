from package import *
class e2fsprogs(MakePackage):
    fetch='http://downloads.sourceforge.net/project/e2fsprogs/e2fsprogs/v1.42.13/e2fsprogs-1.42.13.tar.gz'
    config='./configure --prefix=%(prefix)s --enable-elf-shlibs'
    install="make install && make install-libs"
