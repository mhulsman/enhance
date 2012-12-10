from package import *

class mira(MakePackage):
    dependencies = ['boost','gperftools','flex','expat']
    modify_environ={'LIBRARY_PATH':''}
    fetch="http://downloads.sourceforge.net/project/mira-assembler/MIRA/development/mira-%(version)s.tar.bz2"


