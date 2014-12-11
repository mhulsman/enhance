from package import *

class seqal_python(PythonPackage):
    dependencies = ["git","python"]

    def fetch(self):
        runCommand("git clone https://github.com/mhulsman/seqal.git")

    workdir="seqal"

    unpack=""

        
