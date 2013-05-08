from package import *

class pasa(MakePackage):
    dependencies = ['perl','mysql','gmap','fasta']
    fetch="http://downloads.sourceforge.net/project/pasa/PASA_r2012-06-25.tgz"
    modules = ['DBD::mysql']

    def config(self):
        for module in self.modules:
            runCommand(self.fillVars('PERL_MM_USE_DEFAULT=1 INC="-I%(prefix)s/include" cpan ') +  module )

    build = """
            mkdir -p %(prefix)s/opt/pasa
            cp -R * %(prefix)s/opt/pasa
            cd %(prefix)s/opt/pasa
            make
            """

    install="""
            cp -rs %(prefix)s/opt/pasa/bin/* %(prefix)s/bin/
            cat %(rootpath)s/paths | grep -v PASAHOME > temppath
            echo "export PASAHOME=%(prefix)s/opt/pasa" >> temppath
            cp temppath %(rootpath)s/paths
            """
