from package import *

class ipython(EasyInstallPackage):
    dependencies = ["twisted","foolscap","pyopenssl"]
    
    install="""
            easy_install http://archive.ipython.org/release/0.10.2/ipython-0.10.2.tar.gz
            sed -i -e "s:511:5511:g" %(prefix)s/lib/python2.7/site-packages/ipython-0.10.1-py2.7.egg/IPython/kernel/controllerservice.py 
            """
