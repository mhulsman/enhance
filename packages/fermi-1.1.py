from package import *

class fermi(MakePackage):
  
  dependencies=[]

  fetch='https://github.com/downloads/lh3/fermi/fermi-1.1.tar.bz2'
  
  workdir="fermi-1.1"

  config=""

  install="""
    cp fermi run-fermi.pl %(prefix)s/bin
    """
