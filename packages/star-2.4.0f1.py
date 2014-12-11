from package import *

class star(MakePackage):
    fetch="https://github.com/alexdobin/STAR/archive/STAR_2.4.0f1.tar.gz"
    workdir="STAR-STAR_2.4.0f1/source"
    config=""
    install="cp STAR %(prefix)s/bin/"


