from package import *

class hbardtk(PythonPackage):
    dependencies = ["git","pbh5tools","pbcore","pbdagcon","pypeflow"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/HBAR-DTK.git")

    workdir="HBAR-DTK"

    unpack=""
