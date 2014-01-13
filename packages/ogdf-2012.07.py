from package import *

class ogdf(MakePackage):
  fetch="http://www.ogdf.net/lib/exe/fetch.php/tech:ogdf.v2012.07.zip"
 
  workdir="OGDF"

  config="./makeMakefile.sh"
 
  build="make"

  install="""
	cp _release/libOGDF.a %(prefix)s/lib64
	cp -R ogdf %(prefix)s/include
    """
