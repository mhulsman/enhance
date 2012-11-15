from package import *

class apiextractor(MakePackage):
    dependencies=['qt','libxml','libxslt','python','cmake']
    fetch="https://distfiles.macports.org/apiextractor/apiextractor-%(version)s.tar.bz2"
    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}

    build_reldir = "build"
    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

