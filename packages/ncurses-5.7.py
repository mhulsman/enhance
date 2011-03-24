from package import *

class ncurses(MakePackage):
    fetch="http://ftp.gnu.org/pub/gnu/ncurses/ncurses-%(version)s.tar.gz"
    
    config='./configure --enable-shared --prefix=%(prefix)s CFLAGS="-fPIC"'
        
    install="""
            make install
            cp %(prefix)s/include/ncurses/curses.h %(prefix)s/include/curses.h
            cp %(prefix)s/include/ncurses/ncurses.h %(prefix)s/include/ncurses.h
            cp %(prefix)s/include/ncurses/panel.h %(prefix)s/include/panel.h
            """
