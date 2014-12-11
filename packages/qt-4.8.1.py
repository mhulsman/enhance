from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch="ftp://ftp.qt-project.org/qt/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
