from package import *

class mysql_python(EasyInstallPackage):
    dependencies = ["libmysql","setuptools"]
    install="easy_install mysql-python"

