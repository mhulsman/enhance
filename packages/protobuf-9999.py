from package import *

class protobuf(MakePackage):
    dependencies=['gcc']

    def fetch(self):
        runCommand("git clone https://github.com/google/protobuf")
    
    unpack=""
    workdir="protobuf"

    config="""./autogen.sh
              ./configure --prefix=%(prefix)s
    """
