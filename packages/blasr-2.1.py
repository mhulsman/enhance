from package import *

class blasr(MakePackage):
  
  dependencies=['hdf5']
  fetch='https://github.com/PacificBiosciences/blasr/archive/smrtanalysis-2.1.tar.gz' 
  
  workdir="blasr-smrtanalysis-2.1"

  config="patch common.mk %(distpath)s/packages/blasr-2.1.patch"

  install="""
    rm alignment/bin/*.o
    cp alignment/bin/* %(prefix)s/bin
    """
