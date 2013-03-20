from package import *

class repeatmasker(Package):
    dependencies = ['perl','trf','rmblast']
    fetch='http://www.repeatmasker.org/RepeatMasker-open-4-0-1.tar.gz'

    workdir='RepeatMasker'
    #            wget http://www.girinst.org/server/RepBase/protected/repeatmaskerlibraries/repeatmaskerlibraries-20120418.tar.gz
    #            tar -xzvf repeatmaskerlibraries-20120418.tar.gz

    config="""
            cd Libraries
            wget ftp://selab.janelia.org/pub/dfam/Release/Dfam_1.1/Dfam.hmm.gz
            rm Dfam.hmm
            gunzip Dfam.hmm.gz
            """

    install="""
            mkdir -p %(prefix)s/opt/repeatmasker
            cp -R * %(prefix)s/opt/repeatmasker
            cd %(prefix)s/opt/repeatmasker
            perl ./configure
            ln -f -s ../opt/repeatmasker/RepeatMasker %(prefix)s/bin/
            """

