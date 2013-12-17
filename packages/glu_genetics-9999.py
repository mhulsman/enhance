from package import *


class glu_genetics(PythonPackage):
    dependencies = ['python', 'mercurial','numpy','scipy','pytables', 'ply', 'sqlite']

    def fetch(self):
        runCommand('hg clone https://code.google.com/p/glu-genetics/')

    unpack=""
    workdir="glu-genetics"
