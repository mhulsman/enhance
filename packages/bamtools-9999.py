from package import *

class bamtools(MakePackage):
    dependencies=['git','cmake']

    def fetch(self):
        runCommand('git clone git://github.com/pezmaster31/bamtools.git')
   
    unpack=""
    workdir='bamtools'

    config="""
        mkdir build
        cd build
        cmake ..
    """

    build="""
        cd build
        make
        """

    install="""
    cp -R ./bin/* %(prefix)s/bin/
    cp -R ./lib/* %(prefix)s/lib/
    cp -R ./include/* %(prefix)s/include/
    """    
