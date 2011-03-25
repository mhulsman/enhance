
from package import *

class libmysql(MakePackage):
    dependencies = ["cmake"]
    
    fetch="http://dev.mysql.com/get/Downloads/Connector-C/mysql-connector-c-6.0.2.tar.gz/from/http://ftp.gwdg.de/pub/misc/mysql/"

    config='cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%(prefix)s'

