from package import *


class cmake(MakePackage):
    fetch='http://www.cmake.org/files/v3.0/cmake-3.0.2.tar.gz'

    config="./bootstrap --prefix=%(prefix)s"

