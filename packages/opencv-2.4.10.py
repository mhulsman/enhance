from package import *

class opencv(MakePackage):
    dependencies = ["cmake"]
    fetch="http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-%(version)s.zip"
    workdir="opencv-2.4.10"
    config="""
        mkdir build
	cd build 
        cmake -DBUILD_TIFF=ON -D WITH_EIGEN=OFF -DWITH_CUDA=OFF -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=%(prefix)s ..
    """
    build="""
        cd build
        make
        """
    install="""
        cd build
        make install
        """
