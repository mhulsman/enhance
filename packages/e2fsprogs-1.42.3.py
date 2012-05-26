from package import *
class e2fsprogs(MakePackage):
    fetch='http://kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v1.42.3/e2fsprogs-1.42.3.tar.gz'
    config='./configure --prefix=%(prefix)s --enable-elf-shlibs'
    install="make install && make install-libs"
