from package import *


class fastqc(Package):
    fetch="http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.10.1.zip"
    workdir='FastQC'    

    build="""
    mkdir -p %(prefix)s/opt/fastqc
    cp -R * %(prefix)s/opt/fastqc
    """

    install="""
    cd %(prefix)s/opt/fastqc 
    ln -f -s ../opt/fastqc/fastqc %(prefix)s/bin/
    """

