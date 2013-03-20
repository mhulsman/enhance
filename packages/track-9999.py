from package import *

class track(PythonPackage):
    dependencies = ["git","genomes"]

    def fetch(self):
        runCommand("git clone https://github.com/xapple/track.git")

    workdir="track"

    unpack=""

        
