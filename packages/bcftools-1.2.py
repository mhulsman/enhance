from package import *

class bcftools(Package):
    fetch="http://downloads.sourceforge.net/project/samtools/samtools/1.2/bcftools-1.2.tar.bz2"
    dependencies = ['zlib']
    build="make"
    build="""
        make
        mkdir -p %(prefix)s/opt/bcftools_1.2_plugins
        cp -R plugins/*.so %(prefix)s/opt/bcftools_1.2_plugins
    """
 
    install="""
        make prefix=%(prefix)s install
        cat %(rootpath)s/paths | grep -v BCFTOOLS_PLUGINS > temppath
        echo "export BCFTOOLS_PLUGINS=%(prefix)s/opt/bcftools_1.2_plugins" >> temppath
        cp temppath %(rootpath)s/paths
    """
