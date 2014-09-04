from package import *

class igvtools(Package):
    dependencies = []
    fetch="http://www.broadinstitute.org/igv/projects/downloads/igvtools_2.3.32.zip"
    workdir='IGVTools'
    config = ""
    build=""
    install = """
            mkdir -p %(prefix)s/opt/igvtools
            cp -R * %(prefix)s/opt/igvtools
            cd %(prefix)s/opt/igvtools
            cp -rs %(prefix)s/opt/igvtools/igvtools %(prefix)s/bin/
            cp -rs %(prefix)s/opt/igvtools/igvtools.jar %(prefix)s/bin/
              """  

