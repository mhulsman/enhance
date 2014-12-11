from package import *

class dmd(Package):
    fetch="http://downloads.dlang.org/releases/2014/dmd.2.066.1.zip"

    workdir = "dmd2/linux"

    config = """
        cd bin64
        patch -p0 < %(distpath)s/packages/dmd.conf.patch
        """

    install = """
        cp bin64/* %(prefix)s/bin/
        cp lib64/* %(prefix)s/lib64/
        cd ../src
        mkdir -p %(prefix)s/opt/dmd
        cp -R phobos %(prefix)s/opt/dmd/
        cp -R druntime %(prefix)s/opt/dmd/
    """
