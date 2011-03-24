from package import *

class nlgrid_jdl(Package):
    dependencies = ["cluster_storage"]
   
    workdir="%(rootpath)s/nlgrid_jdl"

    install = """
              cp %(distpath)s/packages/nlgrid_jdl/load_env_worker.sh %(rootpath)s/nlgrid_jdl
              cp %(distpath)s/packages/nlgrid_jdl/load_env.sh %(rootpath)s/nlgrid_jdl
              cp %(distpath)s/packages/nlgrid_jdl/load_env.jdl %(rootpath)s
              cp %(distpath)s/packages/nlgrid_jdl/upload_env.sh %(rootpath)s
              cp %(distpath)s/paths %(prefix)s/_paths
              chmod 755 %(rootpath)s/upload_env.sh
              chmod 755 %(rootpath)s/nlgrid_jdl/load_env.sh
              chmod 755 %(rootpath)s/nlgrid_jdl/load_env_worker.sh
              """ 
   
