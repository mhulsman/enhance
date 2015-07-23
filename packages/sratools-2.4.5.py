from package import *

class sratools(MakePackage):

  fetch = "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.4.5-2/sratoolkit.2.4.5-2-ubuntu64.tar.gz";

  def unpack(self, *p):
    c = """
        mkdir sratools
        cd sratools
        tar -xvf %(srcpath)s/sratoolkit.2.4.5-2-ubuntu64.tar.gz
    """;
    c = self.fillVars(c)
    runCommand(c);
    return 'sratools';
 
  workdir="sratools/sratoolkit.2.4.5-2-ubuntu64/bin"

  config=""

  build="";

  def install(self):
    c="""pwd
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/abi-dump.2.4.5 %(prefix)s/bin/abi-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/abi-load.2.4.5 %(prefix)s/bin/abi-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/align-info.2.4.5 %(prefix)s/bin/align-info
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/bam-load.2.4.5 %(prefix)s/bin/bam-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/blastn_vdb.2.2.30-2.4.5 %(prefix)s/bin/blastn_vdb
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/cache-mgr.2.4.5 %(prefix)s/bin/cache-mgr
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/cg-load.2.4.5 %(prefix)s/bin/cg-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/fastq-dump.2.4.5 %(prefix)s/bin/fastq-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/fastq-load.2.4.5 %(prefix)s/bin/fastq-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/helicos-load.2.4.5 %(prefix)s/bin/helicos-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/illumina-dump.2.4.5 %(prefix)s/bin/illumina-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/illumina-load.2.4.5 %(prefix)s/bin/illumina-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/kar.2.4.5 %(prefix)s/bin/kar
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/kdbmeta.2.4.5 %(prefix)s/bin/kdbmeta
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/latf-load.2.4.5 %(prefix)s/bin/latf-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/pacbio-load.2.4.5 %(prefix)s/bin/pacbio-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/prefetch.2.4.5 %(prefix)s/bin/prefetch
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/rcexplain.2.4.5 %(prefix)s/bin/rcexplain
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/remote-fuser.2.4.5 %(prefix)s/bin/remote-fuser
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sam-dump.2.4.5 %(prefix)s/bin/sam-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sff-dump.2.4.5 %(prefix)s/bin/sff-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sff-load.2.4.5 %(prefix)s/bin/sff-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sra-kar.2.4.5 %(prefix)s/bin/sra-kar
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sra-pileup.2.4.5 %(prefix)s/bin/sra-pileup
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sra-sort.2.4.5 %(prefix)s/bin/sra-sort
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/sra-stat.2.4.5 %(prefix)s/bin/sra-stat
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/srapath.2.4.5 %(prefix)s/bin/srapath
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/srf-load.2.4.5 %(prefix)s/bin/srf-load
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/tblastn_vdb.2.2.30-2.4.5 %(prefix)s/bin/tblastn_vdb
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/test-sra.2.4.5 %(prefix)s/bin/test-sra
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-config.2.4.5 %(prefix)s/bin/vdb-config
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-copy.2.4.5 %(prefix)s/bin/vdb-copy
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-decrypt.2.4.5 %(prefix)s/bin/vdb-decrypt
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-dump.2.4.5 %(prefix)s/bin/vdb-dump
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-encrypt.2.4.5 %(prefix)s/bin/vdb-encrypt
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-lock.2.4.5 %(prefix)s/bin/vdb-lock
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-passwd.2.4.5 %(prefix)s/bin/vdb-passwd
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-unlock.2.4.5 %(prefix)s/bin/vdb-unlock
         cp %(srcpath)s/sratools/sratoolkit.2.4.5-2-ubuntu64/bin/vdb-validate.2.4.5 %(prefix)s/bin/vdb-validate
    """;
    for cmd in c.split('\n'):
      runCommand(self.fillVars(cmd))
