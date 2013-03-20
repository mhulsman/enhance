from package import *

class sparsehash(MakePackage):

  dependencies=[]

  fetch="https://sparsehash.googlecode.com/files/sparsehash-2.0.2.tar.gz"

  config="./configure --prefix=%(prefix)s"

