from package import *

class ncurses(MakePackage):
    fetch="http://ftp.gnu.org/pub/gnu/ncurses/ncurses-%(version)s.tar.gz"
    config='./configure --with-shared --prefix=%(prefix)s CFLAGS="-fPIC"'
        
    install="""
            make install
            cp %(prefix)s/include/ncurses/curses.h %(prefix)s/include/curses.h
            cp %(prefix)s/include/ncurses/ncurses.h %(prefix)s/include/ncurses.h
            cp %(prefix)s/include/ncurses/panel.h %(prefix)s/include/panel.h
            if [ -f "%(prefix)s/lib/libcurses.so" ]; then
                rm %(prefix)s/lib/libcurses.so
            fi
            ln -s %(prefix)s/lib/libncurses.so %(prefix)s/lib/libcurses.so

            """
