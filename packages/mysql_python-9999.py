from package import *

class mysql_python(EasyInstallPackage):
    dependencies = ["libmysql"]
    install="easy_install mysql-python"

