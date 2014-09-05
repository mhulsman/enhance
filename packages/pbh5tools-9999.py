from package import *

class pbh5tools(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/pbh5tools.git")

    workdir="pbh5tools"

    unpack=""
