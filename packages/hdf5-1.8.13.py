from package import *

class hdf5(MakePackage):
    dependencies = ["zlib"]
    fetch='http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.13/src/hdf5-1.8.13.tar.gz'
    config="./configure --prefix=%(prefix)s --enable-cxx"
