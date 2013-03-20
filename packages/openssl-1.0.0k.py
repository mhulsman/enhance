from package import *

class openssl(MakePackage):
    fetch="http://www.openssl.org/source/openssl-%(version)s.tar.gz"
    
    def config(self):
        q = getCommandOutput('uname -a')
        if platformContains('ppc64'):
            print 'Usin powerpc configure'
            runCommand(self.fillVars("./Configure linux-ppc64  shared --prefix=%(prefix)s"))
        else:
            runCommand(self.fillVars("./config shared --prefix=%(prefix)s"))

    build = "make -j1"
