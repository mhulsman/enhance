from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "atlas","python"]
    fetch="http://downloads.sourceforge.net/project/scipy/scipy/0.13.3/scipy-0.13.3.tar.gz"
