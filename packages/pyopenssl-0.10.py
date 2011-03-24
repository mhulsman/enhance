from package import *

class pyopenssl(PythonPackage):
    dependencies = ["python","openssl"]

    fetch="http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-0.10.tar.gz#md5=34db8056ec53ce80c7f5fc58bee9f093"

    workdir="pyOpenSSL-0.10"

    build="python setup.py build_ext -I%(prefix)s/include/openssl -L%(prefix)s/lib"
