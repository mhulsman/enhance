from package import *

class qt(MakePackage):
    dependencies=['gcc==4.6.2','xorg']
    fetch='https://download.qt.io/archive/qt/4.8/4.8.5/qt-everywhere-opensource-src-4.8.5.tar.gz'
    config='./configure -opensource -confirm-license -prefix %(prefix)s'
