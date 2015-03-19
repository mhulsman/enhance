from package import *

class plinkseq(Package):
    fetch="https://psychgen.u.hpc.mssm.edu/plinkseq_downloads/plinkseq-src-0.10.tgz"
    dependencies = []
    workdir='plinkseq-0.10'
    build="make"

    config = """
    patch -p0 < %(distpath)s/packages/plinkseq-0.10.patch
    """

    install="""
        mkdir %(prefix)s/opt/plinkseq-0.10/
        cp -R * %(prefix)s/opt/plinkseq-0.10
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/behead %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/browser %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/gcol %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/mm %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/mongoose %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/pdas %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/pseq %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/smp %(prefix)s/bin/
        cp -rs %(prefix)s/opt/plinkseq-0.10/build/execs/tab2vcf %(prefix)s/bin/
    """
