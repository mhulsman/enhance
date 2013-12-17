from package import *

class matplotlib_venn(EasyInstallPackage):
    dependencies = ["matplotlib"]

    install="easy_install -U matplotlib-venn"
