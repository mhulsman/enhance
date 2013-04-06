from package import *

class bowtie(MakePackage):
    dependencies=["lapack"]
    modify_environ = {'CXXFLAGS':'-fpermissive'}

    fetch="http://sourceforge.net/projects/bowtie-bio/files/bowtie/0.12.8/bowtie-0.12.8-src.zip/download"

    workdir="bowtie-0.12.8"

    config=""

    build="make"

    install="cp bowtie-build bowtie bowtie-inspect %(prefix)s/bin"

