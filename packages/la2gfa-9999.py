from package import *

class la2gfa(MakePackage):
  
  dependencies=['git']

  def fetch(self):
      runCommand('git clone https://github.com/jts/DALIGNER.git')
 
  workdir="DALIGNER"

  config=""

  install="""
cp LA2gfa %(prefix)s/bin
    """
