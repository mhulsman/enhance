from package import *


class cmake(MakePackage):
    fetch='http://www.cmake.org/files/v2.8/cmake-2.8.4.tar.gz'

    config="./bootstrap --prefix=%(prefix)s"

