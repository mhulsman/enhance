from package import *

class dazzdb(MakePackage):
  
  dependencies=['git']

  fetch="https://github.com/thegenemyers/DAZZ_DB/archive/V1.0.tar.gz"
  
  workdir="DAZZ_DB-1.0"
  
  #def fetch(self):
  #    runCommand('git clone https://github.com/thegenemyers/DAZZ_DB.git')

  config=""

  install="""
cp fasta2DB %(prefix)s/bin
cp DB2fasta %(prefix)s/bin
cp quiva2DB %(prefix)s/bin
cp DB2quiva %(prefix)s/bin
cp DBsplit %(prefix)s/bin
cp DBdust %(prefix)s/bin
cp Catrack %(prefix)s/bin
cp DBshow %(prefix)s/bin
cp DBstats %(prefix)s/bin
cp DBrm %(prefix)s/bin
cp simulator %(prefix)s/bin
cp fasta2DAM %(prefix)s/bin
cp DAM2fasta %(prefix)s/bin
    """
