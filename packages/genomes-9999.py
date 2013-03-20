from package import *

class genomes(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/xapple/genomes")

    workdir="genomes"

    unpack=""

        
