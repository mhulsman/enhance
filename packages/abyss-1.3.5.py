from package import *

class abyss(MakePackage):

  dependencies=["openmpi","sparsehash"]

  fetch="http://www.bcgsc.ca/platform/bioinfo/software/abyss/releases/1.3.5/abyss-1.3.5.tar.gz"

  config="./configure --prefix=%(prefix)s "

