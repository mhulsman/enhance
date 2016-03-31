from package import *

class pyside(MakePackage):
    dependencies=['shiboken']
    fetch="https://pypi.python.org/packages/source/P/PySide/PySide-1.1.2.tar.gz"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

