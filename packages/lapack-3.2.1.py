from package import *

class lapack(Package):
    fetch="http://www.netlib.org/lapack/lapack-%(version)s.tgz"

    config='sed -e "s:OPTS     =:OPTS = -fPIC:g" -e "s:NOOPT    =:NOOPT = -fPIC:g" make.inc.example > make.inc'

    build="""
          make blaslib
          make
          """

    install="""
            cp lapack_LINUX.a %(prefix)s/lib/
            """

