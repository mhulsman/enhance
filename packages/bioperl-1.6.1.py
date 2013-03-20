from package import *

class bioperl(Package):
    dependencies = ["expat",'perl','berkeleydb']
    fetch="http://bioperl.org/DIST/BioPerl-1.6.1.tar.gz"

    config = """
            PERL_MM_USE_DEFAULT=1 cpan Bundle::CPAN
            PERL_MM_USE_DEFAULT=1 cpan Module::Build
            PERL_MM_USE_DEFAULT=1 cpan DB_File
            (echo y;echo o conf prefer_installer MB;echo o conf commit)|cpan
            """

    build = """
            PERL_MM_USE_DEFAULT=1 .perl ./Build.PL
            PERL_MM_USE_DEFAULT=1 ./Build 
           """

    install= """
            PERL_MM_USE_DEFAULT=1 ./Build install
            """

