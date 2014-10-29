from package import *

class shogun(MakePackage):
  
  dependencies=['numpy', 'atlas','lapack','R','perl','eigen','swig', 'cmake']
  fetch = 'http://shogun-toolbox.org/archives/shogun/releases/3.2/sources/shogun-3.2.0.tar.bz2'

  build_reldir = 'build'
  config = 'cmake -DCMAKE_INSTALL_PREFIX=%(prefix)s -DPythonModular=ON ..'
  make = 'make install CMAKE_INSTALL_ALWAYS=1'

  
