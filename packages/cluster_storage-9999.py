from package import *

class cluster_storage(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone git://github.com/mhulsman/cluster_storage.git")

    workdir="cluster_storage"

    unpack=""

        
