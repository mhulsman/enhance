from package import *

class celera_pb(MakePackage):
  
  dependencies=[]

  fetch='http://sourceforge.net/projects/wgs-assembler/files/wgs-assembler/wgs-7.0/wgs-7.0-PacBio-Linux-amd64.tar.bz2'
  
  workdir="wgs-7.0"

  config=""

  build=""

  install="""
    ln -sf %(srcpath)s/wgs-7.0/Linux-amd64/bin/* %(prefix)s/bin/
    """
