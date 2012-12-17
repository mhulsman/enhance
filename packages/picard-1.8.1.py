from package import *


class picard(Package):
    fetch="http://downloads.sourceforge.net/project/picard/picard-tools/1.81/picard-tools-1.81.zip"
    
    build="""
    mkdir -p %(prefix)s/opt/picard
    cp *.jar %(prefix)s/opt/picard
    """

    def install(self):
        import os, stat
        ppath = self.prefixpath + '/opt/picard'
        bpath = self.prefixpath + '/bin'
        print "Picard installed in: " + ppath
        print "Bin directory: " +bpath

        for file in os.listdir(ppath):
            if file.endswith('jar'):
                print "Installing shell script for: " + file
                bn,rest = os.path.splitext(os.path.basename(file))
                filename = self.prefixpath + '/bin/' + bn
                f = open(filename,'w')
                f.write('#!/bin/bash\n')
                f.write('java -Xmx2G -jar %s $@\n' % (ppath + '/' + file))
                f.close()
                os.chmod(filename, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)



