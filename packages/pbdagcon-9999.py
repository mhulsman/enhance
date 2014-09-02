from package import *

class pbdagcon(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/pbdagcon.git")

    workdir="pbdagcon"

    unpack=""
