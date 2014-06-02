from package import *


class gatk_slot(Package):
    def fetch(self):
        f = self.fillVars('%(srcpath)s/GenomeAnalysisTK-3.1.1.tar.bz2')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f
    
    workdir="GenomeAnalysisTK-3.1.1"

    build="""
        mkdir -p %(prefix)s/opt/gatk-%(version)s
        cp -R * %(prefix)s/opt/gatk-%(version)s
        cd %(prefix)s/opt/gatk-%(version)s
        """

    install="""
        cd %(prefix)s/opt/gatk-%(version)s
        echo "#!/bin/bash" > gatk-%(version)s
        echo "java -jar %(prefix)s/opt/gatk-%(version)s/GenomeAnalysisTK.jar \$@" >> gatk-%(version)s
        chmod +x gatk-%(version)s
        cp ./gatk-%(version)s %(prefix)s/bin/
    """ 
    
