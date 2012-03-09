from package import *

class generatorrunner(MakePackage):
    dependencies=['apiextractor']
    fetch="http://www.pyside.org/files/generatorrunner-%(version)s.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

