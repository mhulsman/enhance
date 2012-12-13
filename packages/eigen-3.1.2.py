from package import *

class eigen(Package):
    fetch="http://bitbucket.org/eigen/eigen/get/3.1.2.tar.gz"
    workdir="eigen-eigen-5097c01bcdc4"
    install="cp -R Eigen %(prefix)s/include/"
