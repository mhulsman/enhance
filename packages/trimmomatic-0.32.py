from package import *


class trimmomatic(Package):
    fetch="http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.32.zip"
    
    build="""
    mkdir -p %(prefix)s/opt/trimmomatic
    cp *.jar %(prefix)s/opt/trimmomatic
    """

    def install(self):
        import os, stat
        ppath = self.prefixpath + '/opt/trimmomatic'
        bpath = self.prefixpath + '/bin'
        print "Trimmomatic installed in: " + ppath
        print "Bin directory: " +bpath

        file = 'trimmomatic-0.32.jar'
        print "Installing shell script for: " + file
        bn,rest = os.path.splitext(file)


        filename = self.prefixpath + '/bin/trimmomaticPE' 
        f = open(filename,'w')
        f.write('#!/bin/bash\n')
        f.write('java -Xmx2G -classpath %s org.usadellab.trimmomatic.TrimmomaticPE $@\n' % (ppath + '/' + file))
        f.close()
        os.chmod(filename, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)


        filename = self.prefixpath + '/bin/trimmomaticSE' 
        f = open(filename,'w')
        f.write('#!/bin/bash\n')
        f.write('java -Xmx2G -classpath %s org.usadellab.trimmomatic.TrimmomaticSE $@\n' % (ppath + '/' + file))
        f.close()
        os.chmod(filename, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

