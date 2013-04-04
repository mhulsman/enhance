from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch="http://releases.qt-project.org/qt4/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
