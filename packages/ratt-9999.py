from package import *

class ratt(MakePackage):
    dependencies=['mummer']

    def fetch(self):
        runCommand('svn co https://ratt.svn.sourceforge.net/svnroot/ratt ratt')
   
    unpack=""
    workdir='ratt'

    config=""

    build="""
        mkdir -p %(prefix)s/opt/ratt
        cp -R * %(prefix)s/opt/ratt
        cd %(prefix)s/opt/ratt
        """

    install="""
        cd %(prefix)s/opt/ratt
        ln -f -s ../opt/ratt/start.ratt.sh %(prefix)s/bin/
        cat %(rootpath)s/paths | grep -v RATT_HOME > temppath
        echo "export RATT_HOME=%(prefix)s/opt/ratt" >> temppath
        cp temppath %(rootpath)s/paths
    """ 
