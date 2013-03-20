from package import *

class perl(MakePackage):
  fetch="http://www.cpan.org/src/5.0/perl-5.16.2.tar.gz"
  config="sh Configure -de -Dprefix='%(prefix)s'"

  install="""
          make install
          echo "export PERL5LIB=$(echo %(prefix)s/lib/perl5/site_perl/%(version)s/x86_64-linux:$PERL5LIB | sed -e s/:$//)" >> %(prefix)s/../paths
          
          (echo y;echo o conf makepl_arg \"PREFIX=%(prefix)s\";echo o conf commit)|cpan

          """          

           


