from package import *

class nlgrid_jdl(Package):
    dependencies = ["cluster_tools"]
   
    workdir="%(rootpath)s/nlgrid"

    install = """
              cat %(distpath)s/packages/nlgrid_jdl/enhance_worker | sed s#XXLFCHOMEXX#$LFC_HOME#g > %(rootpath)s/nlgrid/enhance_worker
              cat %(distpath)s/packages/nlgrid_jdl/enhance.jdl | sed s#XXPREFIXXX#%(prefix)s#g > %(rootpath)s/nlgrid/enhance.jdl
              cat %(distpath)s/packages/nlgrid_jdl/upload | sed s#XXPREFIXXX#%(prefix)s#g > %(rootpath)s/upload
              cp %(distpath)s/packages/nlgrid_jdl/README %(rootpath)s/nlgrid/
              cp %(distpath)s/paths %(prefix)s/_paths
              chmod 755 %(rootpath)s/upload
              chmod 755 %(rootpath)s/nlgrid/enhance_worker
              if [ ! -d "../sys_enhance/work" ]; then
                 mkdir ../sys_enhance/work
              fi
              """ 
   
