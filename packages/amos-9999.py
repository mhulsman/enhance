from package import *

class amos(MakePackage):
  
  dependencies=['git','cmake']
  def fetch(self):
    runCommand('git clone git://amos.git.sourceforge.net/gitroot/amos/amos')
  
  unpack=""
  workdir='amos'
 
  config="""
    ./bootstrap
    ./configure --prefix=%(prefix)s
    """
