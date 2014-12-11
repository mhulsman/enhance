from package import *

class shapeit(Package):
    fetch="https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.v2.r790.RHELS_5.4.static.tar.gz"
    def unpack(self, *p):
        c = """
            mkdir shapeit
            cd shapeit
            tar -xzvf %(srcpath)s/shapeit.v2.r790.RHELS_5.4.static.tar.gz
        """
        c = self.fillVars(c)
        runCommand(c)
        return 'shapeit'

    workdir = "shapeit"
    install = "cp shapeit %(prefix)s/bin/"

