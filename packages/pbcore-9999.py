from package import *

class pbcore(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/pbcore.git")

    workdir="pbcore"

    unpack=""
