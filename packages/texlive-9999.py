from package import *;

class texlive(Package):

    import tarfile;

    fetch   = "http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz";
    #workdir = tarfile.open('... where does it go?...').getnames()[0];
    install = "install-tl -gui text";
    modify_environ = "adding texlive path to PATH";
#eclass
