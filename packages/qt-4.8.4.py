from package import *

class qt(MakePackage):
    dependencies=['gcc','xorg']
    fetch='http://pkgs.fedoraproject.org/repo/pkgs/qt/qt-everywhere-opensource-src-%(version)s.tar.gz/89c5ecba180cae74c66260ac732dc5cb/qt-everywhere-opensource-src-%(version)s.tar.gz'
