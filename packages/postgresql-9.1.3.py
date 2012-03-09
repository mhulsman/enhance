from package import *

class postgresql(MakePackage):
    dependencies = ["readline"]
    fetch="http://ftp.postgresql.org/pub/source/v%(version)s/postgresql-%(version)s.tar.gz"


