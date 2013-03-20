from package import *
class mpfr(MakePackage):
    dependencies=['gmp']
    fetch='http://www.mpfr.org/mpfr-current/mpfr-%(version)s.tar.gz'

