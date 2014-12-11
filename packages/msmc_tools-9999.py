from package import *

class msmc_tools(Package):
    dependencies=["msmc"]
    
    def fetch(self):
        runCommand("git clone https://github.com/stschiff/msmc-tools.git")

    workdir = "msmc-tools"

    config =""
    build = ""
    install ="cp *.py %(prefix)s/bin/"


