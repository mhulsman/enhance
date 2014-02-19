from package import *

class bh_tsne(MakePackage):
    dependencies=['gsl']
    fetch="http://homepage.tudelft.nl/19j49/t-SNE_files/bh_tsne.tar.gz"

    def unpack(self,*p):
        c  ="""
            mkdir tsne
            cd tsne
            tar -xzvf %(srcpath)s/bh_tsne.tar.gz
        """
        c = self.fillVars(c)
        runCommand(c)
        return 'tsne'

    workdir="tsne"
    config="""
            cp %(distpath)s/packages/tsne.patch .
            patch -p0 < tsne.patch
            cat compile_linux | sed s#PLACEHOLDER#%(prefix)s/include/# > compile_linux2
           """           

    build="""
            chmod +x ./compile_linux2
            ./compile_linux2
         """

    install="""
            cp %(srcpath)s/tsne/bh_tsne %(prefix)s/bin/
            """


