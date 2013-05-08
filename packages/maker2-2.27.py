from package import *

class maker2(MakePackage):
    dependencies = ['perl','bioperl','ncbi_blast','snap','repeatmasker','exonerate','augustus','genemark_es','zlib','postgresql']
    def fetch(self):
        f = self.fillVars('%(srcpath)s/maker-2.27-beta.tgz')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f

    workdir='maker'


    modules = ['DBI','DBD::SQLite','Proc::ProcessTable','threads','IO::All','IO::Prompt','File::Which','Perl::Unsafe::Signals','Bit::Vector','Inline::C','PerlIO::gzip','Bio::Root::Version','forks','forks::shared','Bio::ASN1::EntrezGene','DBD::Pg','URI::Escape']
    def config(self):
        for module in self.modules:
            runCommand(self.fillVars('PERL_MM_USE_DEFAULT=1 INC="-I%(prefix)s/include" cpan ') +  module )

    build = """
            mkdir -p %(prefix)s/opt/maker2
            cp -R * %(prefix)s/opt/maker2
            cd %(prefix)s/opt/maker2
            cd src
            PERL_MM_USE_DEFAULT=1 perl ./Build.PL
            """

    install="""
            cd %(prefix)s/opt/maker2/src
            ./Build install
            cp -rs %(prefix)s/opt/maker2/bin/* %(prefix)s/bin/
            echo "export PERL5LIB=\$(echo %(prefix)s/opt/maker2/perl/lib:%(prefix)s/opt/maker2/lib:\$PERL5LIB | sed -e s/:$//)" >> %(prefix)s/../paths
            """
