from package import *

class verifybamid(Package):
    fetch="https://github.com/statgen/verifyBamID/releases/download/v1.1.0/verifyBamIDLibStatGen.1.1.0.tgz"
    workdir="verifyBamID_1.1.0"
    build="make"
    config=""
    install="cp verifyBamID/bin/* %(prefix)s/bin/"


