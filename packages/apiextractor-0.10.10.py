from package import *

class apiextractor(MakePackage):
    dependencies=['qt','libxml','libxslt','python','cmake']
    fetch="http://www.pyside.org/files/apiextractor-0.10.10.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

