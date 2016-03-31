from package import *

class pyside(Package):
    dependencies=['cmake', 'python', 'qt', 'libxml', 'libxslt', 'git', 'pip', 'wheel']

    fetch="https://pypi.python.org/packages/source/P/PySide/PySide-%(version)s.tar.gz"

    build="python setup.py bdist_wheel" 
    
    install="""
        pip install --use-wheel %(workpath)s/dist/PySide-%(version)s-cp27-none-linux_x86_64.whl
        python pyside_postinstall.py -install
        """
#    modify_environ = {'PYSIDESANDBOXPATH':'%(prefix)s'}
#
#    build_reldir = "build"
#    config = "cmake .. -DCMAKE_INSTALL_PREFIX=%(prefix)s -DCMAKE_BUILD_TYPE=Release -DENABLE_ICECC=0"

