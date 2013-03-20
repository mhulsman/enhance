from package import *

class genemark_es(Package):
    dependencies = ['perl']
    def fetch(self):
        f = self.fillVars('%(srcpath)s/gm_es_bp_linux64_v2.3e.tar.gz')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        f2 = self.fillVars('%(srcpath)s/gm_key_64.tar')
        if not os.path.isfile(f):
            error('Please supply source file: %s' %f)
        return f

    config="""
            cp %(srcpath)s/gm_key_64.tar .
            tar -xvf gm_key_64.tar
            """

    build="""
        mkdir -p %(prefix)s/opt/genemark_es
        cp -R * %(prefix)s/opt/genemark_es
        cd %(prefix)s/opt/genemark_es
        """

    install="""
        cd %(prefix)s/opt/genemark_es
        ln -f -s %(prefix)s/opt/genemark_es/gmes/gm_es.pl %(prefix)s/bin/
        ln -f -s %(prefix)s/opt/genemark_es/gmes/gmhmme3 %(prefix)s/bin/
        ln -f -s %(prefix)s/opt/genemark_es/gmes/probuild %(prefix)s/bin/
    """        
