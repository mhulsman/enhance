from package import *

class pyside(MakePackage):
    dependencies=['shiboken']
    fetch="http://qt-project.org/uploads/pyside/pyside-qt4.8+%(version)s.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

