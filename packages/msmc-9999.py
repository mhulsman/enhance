from package import *

class msmc(Package):
    dependencies=["dmd","python3"]
    
    def fetch(self):
        runCommand("git clone https://github.com/stschiff/msmc.git")

    workdir = "msmc"

    config ="""
                patch -p0 < %(distpath)s/packages/msmc.makefile.patch
            """
    build = "make -f Makefile.linux"
    install ="cp build/msmc %(prefix)s/bin/"


