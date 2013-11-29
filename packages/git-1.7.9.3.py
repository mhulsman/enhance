from package import *

class git(Package):
    dependencies = ["python",'openssl','zlib','curl']

    fetch="http://git-core.googlecode.com/files/git-1.7.9.3.tar.gz"

    install="make PYTHON_PATH=%(prefix)s/bin/python NO_EXPAT=YesPlease NO_TCLTK=YesPlease PERL_PATH=%(prefix)s/bin/perl prefix=%(prefix)s all install"

