from package import *

class vcflib(MakePackage):
  
  dependencies=['git']

  def fetch(self):
    runCommand('git clone --recursive git://github.com/ekg/vcflib.git')
 
  config=""

  workdir="vcflib"

  install="""
    cp bin/* %(prefix)s/bin/
  """
