from package import *


class scipy(PythonPackage):
    dependencies = ["numpy", "atlas","python"]
    
    fetch="http://downloads.sourceforge.net/project/scipy/scipy/0.11.0/scipy-0.11.0.tar.gz"

    #config="""
    #       wget http://projects.scipy.org/scipy/raw-attachment/ticket/1180/0001-FIX-define-macro-to-access-C99-extensions-from-C.patch
    #       patch -p1 < 0001-FIX-define-macro-to-access-C99-extensions-from-C.patch
    #       """
 
