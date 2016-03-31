from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "atlas","python"]
    fetch="http://downloads.sourceforge.net/project/scipy/scipy/0.16.0/scipy-0.16.0.tar.gz"
