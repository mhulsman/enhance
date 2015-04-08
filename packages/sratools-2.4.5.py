from package import *

class sratools(MakePackage):

  fetch = "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.4.5-2/sratoolkit.2.4.5-2-ubuntu64.tar.gz";

  def unpack(self):
    c = """
        mkdir sratools
        cd sratools
        tar -xvf %(srcpath)s/sratoolkit.2.4.5-2-ubuntu64.tar.gz
     """;
 
  workdir="sratoolkit.2.4.5-2-ubuntu64/bin"

  config=""

  install="""
cp -r `find ./ -executable` /tmp
    """
