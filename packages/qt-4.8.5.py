from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch='http://download.qt-project.org/official_releases/qt/4.8/4.8.5/qt-everywhere-opensource-src-%(version)s.tar.gz'
