from package import *

class ipython(EasyInstallPackage):
    dependencies = ["twisted","foolscap","pyopenssl"]
    
    install="""
            easy_install %(name)s
            sed -i -e "s:511:5511:g" %(prefix)s/lib/python2.7/site-packages/ipython-0.10.1-py2.7.egg/IPython/kernel/controllerservice.py 
            """
