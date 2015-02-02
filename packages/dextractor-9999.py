from package import *

class dextractor(MakePackage):
  
  dependencies=['git']

  def fetch(self):
      runCommand('git clone https://github.com/thegenemyers/DEXTRACTOR.git')
 
  workdir="DEXTRACTOR"

  config=""

  install="""
    cp dexqv %(prefix)s/bin   
    cp dexta %(prefix)s/bin
    cp dextract %(prefix)s/bin
    cp undexqv %(prefix)s/bin
    cp undexta %(prefix)s/bin
    """
