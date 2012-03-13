from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch="http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
