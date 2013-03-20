from package import *

class glib(MakePackage):
    dependencies=['libffi','python','pkgconfig']
    fetch="http://ftp.gnome.org/pub/gnome/sources/glib/2.30/glib-2.30.2.tar.bz2"
