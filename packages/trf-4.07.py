from package import *

class trf(Package):
    def fetch(self):
        f = self.fillVars('%(srcpath)s/trf407b.linux64')
        if not os.path.isfile(f):
            error('Please supply source file: %s. Download from http://tandem.bu.edu/trf/trf.html' %f)

    workdir='%(prefix)s'
    install="""
            cp %(srcpath)s/trf407b.linux64 %(prefix)s/bin/trf
            chmod +x+u %(prefix)s/bin/trf
            """


