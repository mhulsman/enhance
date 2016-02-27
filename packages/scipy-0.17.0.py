from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "openblas","python","cython"]
    fetch="http://sourceforge.net/projects/scipy/files/scipy/0.16.0b2/scipy-0.17.0.tar.gz"
