from package import *

class llvm(MakePackage):
    fetch="http://llvm.org/releases/3.0/llvm-3.0.tar.gz"
    workdir="llvm-3.0.src"
    config="""
           wget http://llvm.org/releases/3.0/clang-3.0.tar.gz
           tar -xzvf clang-3.0.tar.gz
           mv clang-3.0.src tools/clang
           ./configure --prefix=%(prefix)s --enable-jit
           """


