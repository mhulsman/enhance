from package import *

class pytables(EasyInstallPackage):
    dependencies = ["setuptools","python","numpy","hdf5","numexpr"]

    install="easy_install -U tables"
    
