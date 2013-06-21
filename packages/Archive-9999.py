from package import *

class Archive(Package):
    dependencies=['perl']

    def fetch(self):
      pass;

    config=""
    build=""
    
    install="""
      cpan -i Archive::Tar
    """
