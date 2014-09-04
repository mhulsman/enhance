from package import *

class plink(MakePackage):
    dependencies = []
    fetch="http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-1.07-x86_64.zip"
    config = ""
    build=""
    install = """
            mkdir -p %(prefix)s/opt/plink
            cp -R * %(prefix)s/opt/plink
            cd %(prefix)s/opt/plink
            ln -f -s ../opt/plink/plink %(prefix)s/bin/
              """  

