from package import *

class dwgsim(MakePackage):
  
  dependencies=['samtools']
  fetch="http://downloads.sourceforge.net/project/dnaa/dwgsim/dwgsim-0.1.11.tar.gz"
  workdir="dwgsim-0.1.11"
  build="make CC=/usr/bin/gcc"
  config="ln -s %(srcpath)s/samtools-0.1.18 samtools"
  install="cp dwgsim dwgsim_eval %(prefix)s/bin"
