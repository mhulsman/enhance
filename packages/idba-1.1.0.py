from package import *

class idba(MakePackage):
  fetch="http://hku-idba.googlecode.com/files/idba-1.1.0.tar.gz"
  install="""
    cp bin/filterfa bin/fq2fa bin/idba bin/idba_tran bin/idba_ud bin/parallel_blat bin/raw_n50 bin/sim_reads bin/sim_reads_tran bin/split_scaffold bin/validate_contigs_blat  %(prefix)s/bin/
  """
