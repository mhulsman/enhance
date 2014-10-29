from package import *

class ngsutils(MakePackage):

    def fetch(self):
        runCommand('git clone git://github.com/ngsutils/ngsutils.git')

    workdir="ngsutils"

    config=""

    build="make"
