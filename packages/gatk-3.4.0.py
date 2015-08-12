from package import *


class gatk(Package):
    dependencies = ['jre_oracle']
    def fetch(self):
        f = self.fillVars('%(srcpath)s/GenomeAnalysisTK-3.4-0.tar.bz2')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f
    
    workdir="gatk-3.4-0"
    create_workdir=True

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
    
