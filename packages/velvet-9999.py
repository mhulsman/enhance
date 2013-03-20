from package import *

class velvet(MakePackage):
  
  dependencies=['git','cmake']
  def fetch(self):
    runCommand('git clone git://github.com/dzerbino/velvet.git')
 
  def Config(self) :
     
  build="""
    make 'MAXKMERLENGTH=96' 'OPENMP=1'
  """
