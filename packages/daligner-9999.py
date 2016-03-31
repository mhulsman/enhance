from package import *

class daligner(MakePackage):
  
  dependencies=['git']
  
  fetch="https://github.com/thegenemyers/DALIGNER/archive/V1.0.tar.gz"
  #def fetch(self):
  #    runCommand('git clone https://github.com/thegenemyers/DALIGNER.git')
 
  workdir="DALIGNER-1.0"

  config=""

  install="""
cp daligner %(prefix)s/bin
cp HPCdaligner %(prefix)s/bin
cp HPCmapper %(prefix)s/bin
cp LAsort %(prefix)s/bin
cp LAmerge %(prefix)s/bin
cp LAsplit %(prefix)s/bin
cp LAcat %(prefix)s/bin
cp LAshow %(prefix)s/bin
cp LAcheck %(prefix)s/bin
    """
