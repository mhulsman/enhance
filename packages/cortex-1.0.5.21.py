from package import *

class cortex(MakePackage):
  
  dependencies=['stampy','vcftools']

  fetch='http://downloads.sourceforge.net/project/cortexassembler/cortex_var/latest/CORTEX_release_v1.0.5.21.tgz'
  
  config="""
    bash install.sh
  """

  build="""
    make NUM_COLS=1 cortex_var
    make NUM_COLS=2 cortex_var
    make NUM_COLS=1 MAXK=63 cortex_var
    make NUM_COLS=2 MAXK=63 cortex_var
  """

  install="""
    cp -rf %(srcpath)s/CORTEX_release_v1.0.5.21 %(prefix)s/opt
    """
