from package import *

class ant(MakePackage):
  
  dependencies=['']
  fetch='http://apache.mirror1.spango.com//ant/source/apache-ant-1.9.4-src.tar.gz'
  
  install="./build.sh install-lite"
