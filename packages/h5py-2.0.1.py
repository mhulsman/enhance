from package import *

class h5py(PythonPackage):
    dependencies = ["hdf5"]

    fetch="http://h5py.googlecode.com/files/h5py-2.0.1.tar.gz"

    build="python setup.py build --hdf5=%(prefix)s"
