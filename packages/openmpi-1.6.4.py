from package import *

class openmpi(MakePackage):

  dependencies=[]

  fetch="http://www.open-mpi.org/software/ompi/v1.6/downloads/openmpi-1.6.4.tar.bz2"

  config="./configure --prefix=%(prefix)s"

  build = "make all"
