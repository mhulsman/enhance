from package import *

class libxslt(MakePackage):
    dependencies = ['libxml']
    fetch="ftp://xmlsoft.org/libxslt/libxslt-1.1.28.tar.gz"
