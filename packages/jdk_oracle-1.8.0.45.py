from package import *

class jdk_oracle(Package):
    dependencies=[]
   
    def fetch(self):
        runCommand('wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz -O jdk-8u45-linux-x64.tar.gz')
        return "jdk-8u45-linux-x64.tar.gz"

    workdir='jdk1.8.0_45'

    install="""
                mv lib lib64
                rsync -av * %(prefix)s
                rsync -av lib64/amd64/* %(prefix)s/lib64/
            """ 
