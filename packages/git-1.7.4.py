from package import *

class git(Package):
    dependencies = ["python"]

    fetch="http://www.kernel.org/pub/software/scm/git/git-1.7.4.tar.gz"

    install="make PYTHON_PATH=%(prefix)s/bin/python NO_EXPAT=YesPlease NO_TCLTK=YesPlease prefix=%(prefix)s all install"

