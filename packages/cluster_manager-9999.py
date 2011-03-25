from package import *

class cluster_manager(Package):
    dependencies = ["cluster_tools","nlgrid_jdl"]
    
    def fetch(self):
        runCommand("git clone git://github.com/mhulsman/cluster_manager.git")
  
    workdir="cluster_manager"

    def install(self):
        mkpath(os.path.join(self.prefixpath, 'usr/local/cluster_manager'))
        import cluster_storage
        import inspect
        cl_path = os.path.join(os.path.dirname(inspect.getfile(cluster_storage)),"cluster_storage.py")
        print "Detecting cluster_storage path: ", cl_path
        
        if os.path.isfile(os.path.join(self.prefixpath,'bin/cluster')):
            os.remove(os.path.join(self.prefixpath,'bin/cluster'))

        cmd = """
        cp * %(prefix)s/usr/local/cluster_manager
        cat ipengine.jdl | sed s#XXAPPPATHXX#%(prefix)s/usr/local/cluster_manager#g > %(prefix)s/usr/local/cluster_manager/ipengine.jdl
        cat ipython_engine | sed s#XXAPPPATHXX#%(prefix)s/usr/local/cluster_manager#g > %(prefix)s/usr/local/cluster_manager/ipython_engine
        
        cp %(prefix)s/bin/gcp %(prefix)s/usr/local/cluster_manager/
        cp %(cl_path)s %(prefix)s/usr/local/cluster_manager/

        chmod 755 %(prefix)s/usr/local/cluster_manager/cluster
        chmod 755 %(prefix)s/usr/local/cluster_manager/ipengine_chief
        chmod 755 %(prefix)s/usr/local/cluster_manager/load_env_ipengine.sh
        
        cp %(prefix)s/usr/local/cluster_manager/ipengine_chief %(prefix)s/work
        ln -s %(prefix)s/usr/local/cluster_manager/cluster %(prefix)s/bin/cluster
        """

        runCommand(self.fillVars(cmd,cl_path=cl_path))


