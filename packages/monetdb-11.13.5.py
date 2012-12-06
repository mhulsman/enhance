from package import *


class monetdb(MakePackage):
    dependencies = ['openssl','pcre','bison','libxml']
    fetch='http://dev.monetdb.org/downloads/sources/Latest/MonetDB-%(version)s.zip'
