from package import *

class shogun(MakePackage):
  
  dependencies=['numpy', 'atlas','lapack','R','perl','eigen','swig']
  fetch = 'http://shogun-toolbox.org/archives/shogun/releases/3.0/sources/shogun-3.0.0.tar.bz2'

  build_reldir = 'build'
  config = 'cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Debug -DPythonModular=ON -DPythonStatic=ON'

  
