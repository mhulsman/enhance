from package import *


class monetdb(MakePackage):
    dependencies = ['openssl']
    fetch='http://dev.monetdb.org/downloads/sources/Latest/MonetDB-11.9.5.zip'
