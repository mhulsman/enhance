from package import *

class pypeflow(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/cschin/pypeFLOW.git")

    workdir="pypeFLOW"

    unpack=""
