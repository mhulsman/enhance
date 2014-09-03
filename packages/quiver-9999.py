from package import *

class quiver(PythonPackage):
    dependencies = ["git","boost","swig","consensuscore"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/GenomicConsensus")

    workdir="ConsensusCore"

    unpack=""

