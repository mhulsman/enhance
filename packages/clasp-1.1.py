from package import *

class clasp(MakePackage):
    fetch="http://www.bioinf.uni-leipzig.de/Software/clasp/clasp_v1_1.tar.gz"
    
    def Config(self) :
        pass

    install= """
        cp clasp.x %(prefix)s/bin/
    """
