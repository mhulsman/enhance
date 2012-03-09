from package import *

class shiboken(MakePackage):
    dependencies=['apiextractor', 'generatorrunner']
    fetch="http://www.pyside.org/files/shiboken-1.1.0.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

