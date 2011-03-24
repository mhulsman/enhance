from package import *

class sqlite(MakePackage):
    fetch="http://www.sqlite.org/sqlite-amalgamation-%(version)s.tar.gz"

    workdir="sqlite-3.7.3"
