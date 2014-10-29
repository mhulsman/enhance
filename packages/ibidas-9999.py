from package import *

#class ibidas(PythonPackage):
#    dependencies = ["git",'ipython','numpy','pyparsing']
#
#    def fetch(self):
#        runCommand("git clone https://github.com/mhulsman/ibidas")
#
#    unpack  = ""
#    workdir = "ibidas"

class ibidas(EasyInstallPackage):
    dependencies = ['ipython','numpy','pyparsing']
