
from package import *

class mysql(MakePackage):
    dependencies = ["cmake"]
    fetch="http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.10.tar.gz/from/http://cdn.mysql.com/"
    config='cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%(prefix)s -DWITH_READLINE=1'

