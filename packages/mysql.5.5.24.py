
from package import *

class mysql(MakePackage):
    dependencies = ["cmake"]
    
    fetch="http://www.mysql.com/get/Downloads/MySQL-5.5/mysql-5.5.24.tar.gz/from/http://mirror.leaseweb.com/mysql/"

    config='cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%(prefix)s'

