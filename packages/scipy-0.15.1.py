from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "atlas","python"]
    fetch="http://downloads.sourceforge.net/project/scipy/scipy/0.15.1/scipy-0.15.1.tar.gz"
