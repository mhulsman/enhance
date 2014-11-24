from package import *

class libdivsufsort(MakePackage):
  
  dependencies=['cmake']

  fetch='https://libdivsufsort.googlecode.com/files/libdivsufsort-2.0.1.tar.gz'
  
  workdir="libdivsufsort-2.0.1"

  config="""
	mkdir build
	cd build
	cmake -DCMAKE_BUILD_TYPE=\"Release\" -DCMAKE_INSTALL_PREFIX=\"%(prefix)s\" -DBUILD_DIVSUFSORT64:BOOL=ON ..
	"""

  build="""
	cd build
	make
	"""

  install="""
	cd build
	make install
	"""
