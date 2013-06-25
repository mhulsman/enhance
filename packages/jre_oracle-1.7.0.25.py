from package import *

class jre_oracle(Package):
    dependencies=[]
    
    def fetch(self):
        f = self.fillVars('%(srcpath)s/jre-7u25-linux-x64.tar.gz')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f
  
    workdir='jre1.7.0_25'

    install="""
                mv lib lib64
                rsync -av * %(prefix)s
                rsync -av lib64/amd64/* %(prefix)s/lib64/
                
            """ 
