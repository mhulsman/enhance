from package import *

class consensuscore(PythonPackage):
    dependencies = ["git","boost","swig"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/ConsensusCore")

    workdir="ConsensusCore"

    unpack=""

    install="python setup.py install --boost=%(prefix)s/include/"
