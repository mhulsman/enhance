from package import *

class numpy(PythonPackage):
    dependencies = ["openblas","python"]
    fetch="http://downloads.sourceforge.net/project/numpy/NumPy/1.10.4/numpy-1.10.4.tar.gz"

    site="""
[DEFAULT]
library_dirs = %(prefix)s/lib
include_dirs = %(prefix)s/include

[openblas]
libraries = openblas
library_dirs = %(prefix)s/lib
include_dirs = %(prefix)s/include
"""

    def config(self):
        sitecfg = self.fillVars(self.site)
        f = open(os.path.join(self.workdir, 'site.cfg'),'w')
        f.write(sitecfg)
        f.close()
