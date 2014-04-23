from package import *

class circos(MakePackage):
    dependencies = ['perl','libgd']
 
    fetch="http://circos.ca/distribution/circos-0.66.tgz"
    modules = ['Config::General','Clone', 'Font::TTF','GD','List::MoreUtils','Math::Bezier','Math::Round','Math::VecStat','Params::Validate','Readonly','Regexp::Common','Set::IntSpan','Text::Format']
    
    
    def config(self):
        for module in self.modules:
            runCommand(self.fillVars('PERL_MM_USE_DEFAULT=1 INC="-I%(prefix)s/include" cpan ') +  module )

    build = """
            mkdir -p %(prefix)s/opt/circos
            cp -R * %(prefix)s/opt/circos
            """

    install="""
            cd %(prefix)s/opt/circos
            cp -rs %(prefix)s/opt/circos/bin/* %(prefix)s/bin/
            """
