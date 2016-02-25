from package import *

class bedops(Package):
    dependencies=['gcc==4.6.2','git']

    fetch="https://github.com/bedops/bedops/releases/download/v2.4.2/bedops_linux_x86_64-v2.4.2.tar.bz2"
    workdir='bin'

    install="""
    cp -R * %(prefix)s/bin/
    """



