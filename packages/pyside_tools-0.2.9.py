from package import *

class pyside_tools(MakePackage):
    dependencies=['pyside']
    fetch="http://www.pyside.org/files/pyside-tools-0.2.9.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

