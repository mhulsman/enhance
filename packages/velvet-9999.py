from package import *

class velvet(MakePackage):
  
  dependencies=['git']
  def fetch(self):
    runCommand('git clone git://github.com/dzerbino/velvet.git')
 
  def Config(self) :
    pass
    
  build="""
    cd velvet
    make 'MAXKMERLENGTH=96' 'OPENMP=1'"""  
  install="""
    cp velvetg %(prefix)s/bin/
    cp velveth %(prefix)s/bin/
  """
