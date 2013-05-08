from package import *


class gatk(Package):
    def fetch(self):
        f = self.fillVars('%(srcpath)s/GenomeAnalysisTK-2.4-9.tar.bz2')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f
    
    workdir="GenomeAnalysisTK-2.4-9-g532efad"

    build="""
        mkdir -p %(prefix)s/opt/gatk
        cp -R * %(prefix)s/opt/gatk
        cd %(prefix)s/opt/gatk
        """

    install="""
        cd %(prefix)s/opt/gatk
        echo "#!/bin/bash" > gatk
        echo "java -jar %(prefix)s/opt/gatk/GenomeAnalysisTK.jar \$@" >> gatk
        chmod +x gatk
        cp ./gatk %(prefix)s/bin/
    """ 
    
