from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "openblas","python","cython"]
    fetch="https://github.com/scipy/scipy/archive/v0.17.0.tar.gz"
    workdir="scipy-0.17.0"
