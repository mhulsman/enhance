from package import *;

class numexpr(PythonPackage):
    dependencies = ["python","numpy"]
    fetch="https://github.com/pydata/numexpr/archive/v2.3.1.tar.gz"
    workdir="numexpr-2.3.1"
