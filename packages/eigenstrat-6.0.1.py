from package import *
class eigenstrat(Package):
    fetch='ftp://pricelab:pricelab@ftp.broadinstitute.org/EIGENSOFT/EIG6.0.1.tar.gz'

    install="""
            cp  ./bin/* %(prefix)s/bin/
            """

