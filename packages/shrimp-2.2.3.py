from package import *

class shrimp(Package):
    fetch="http://compbio.cs.toronto.edu/shrimp/releases/SHRiMP_2_2_3.lx26.x86_64.tar.gz"

    workdir="SHRiMP_2_2_3"

    install="""
    mkdir %(prefix)s/opt/shrimp/
    cp -R * %(prefix)s/opt/shrimp/
    cp -rs %(prefix)s/opt/shrimp/bin/* %(prefix)s/bin
    """
    
    
