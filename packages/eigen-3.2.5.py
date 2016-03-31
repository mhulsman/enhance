from package import *

class eigen(Package):
    fetch="http://bitbucket.org/eigen/eigen/get/3.2.5.tar.gz"
    workdir="eigen-eigen-bdd17ee3b1b3"
    install="cp -R Eigen %(prefix)s/include/"
