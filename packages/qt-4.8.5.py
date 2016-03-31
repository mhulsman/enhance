from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch='https://download.qt.io/archive/qt/4.8/4.8.5/qt-everywhere-opensource-src-4.8.5.tar.gz' 
    config='./configure -prefix %(prefix)s -fast -no-webkit -no-qt3support -nomake examples -nomake docs -nomake demos -opensource -confirm-license'
