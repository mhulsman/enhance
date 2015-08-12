from package import *;

class texlive(Package):

    import tarfile;

    fetch   = "http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz";
    def workdir(self, package_file):
        return tarfile.open(package_file).getnames()[0];

    modify_environ = {'TEXLIVE_INSTALL_PREFIX':'%(prefix)s/opt/tex'}

    install = "./install-tl -gui text -portable";

#eclass:w

