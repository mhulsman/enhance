from package import *

class stampy(MakePackage):
  
  dependencies=[]

  fetch='http://www.well.ox.ac.uk/~gerton/software/Stampy/stampy-1.0.23r2059.tgz'

  workdir='stampy-1.0.23'

  config='patch makefile %(distpath)s/packages/stampy.1.0.23.patch'

  install='''
   mkdir %(prefix)s/opt/stampy-1.0.23
   cp -rf * %(prefix)s/opt/stampy-1.0.23
  '''
