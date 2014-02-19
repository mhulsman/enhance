from package import *

class marygold(MakePackage):
  
  dependencies=['boost','amos','ogdf','numpy','scipy','editdist','biopython']
  def fetch(self):
    runCommand('git clone git://git.code.sf.net/p/metavar/code metavar-code')
  
  unpack=""
  workdir="metavar-code"

  #remove patch when repo is updated...
  config="""
    patch configure.ac < %(distpath)s/packages/marygold-9999_20140113.patch
    patch -p0 < %(distpath)s/packages/marygold-9999_20140113_unistd.patch
    ./bootstrap
    ./configure --prefix=%(prefix)s --with-AMOS-include-path=%(prefix)s/include/AMOS --with-AMOS-lib-path=%(prefix)s/lib/AMOS/ --with-BOOST-include-path=%(prefix)s/include/boost --with-BOOST-lib-path=%(prefix)s/lib64/ --with-OGDF-include-path=%(prefix)s/include/ --with-OGDF-lib-path=%(prefix)s/lib64/
    """
