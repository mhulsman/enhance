from package import *

class dwgsim(MakePackage):
  
  dependencies=['samtools']
  fetch="http://downloads.sourceforge.net/project/dnaa/dwgsim/dwgsim-0.1.10.tar.gz"
  workdir="dwgsim-0.1.10"
  config="ln -s %(srcpath)s/samtools-0.1.18 samtools"
  install="cp dwgsim dwgsim_eval %(prefix)s/bin"
