import subprocess
import tarfile
import zipfile
import gzip
import bz2
import urllib2
import urlparse
import os
from os import path
from distutils.dir_util import mkpath
import sys
import shutil
import inspect

def enter_dir(path):
    check_dir(path)
    oldpath = os.getcwd()
    os.chdir(path)
    return oldpath


def check_dir(path):
    if not os.path.isdir(path):
        assert not os.path.exists(path), "Folder: " + str(path) + " already exists as non-directory"
        mkpath(path)


def url_to_file(url):
    return url.split('/')[-1]
    
def download(url, filename=None):
    if filename is None:
        filename = url_to_file(url)
    
    u = urllib2.urlopen(url)
    f = open(filename, 'w')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (filename, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += block_sz
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

    return filename


def is_gzipfile(filename):
    try:
        gzip.open(filename,'r')
        gzip.close()
        return True
    except Exception:
        return False

def unpack(filename, force=False):
    res = []
    if filename.endswith('.tar.gz'):
        workdir = filename[:-7]
        if os.path.isdir(workdir):
            shutil.rmtree(workdir)
        runCommand("tar -xzf " + filename)
    return workdir

def runCommand(cmd):
    res = subprocess.call(cmd,shell=True)
    if not res == 0:
        raise RuntimeError, "Command failed"

def getCommandOutput(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p.stdout.read().strip()

def error(msg):
    print "\033[41mERROR: " + msg + "\033[0m"
    sys.exit(1)

def warning(msg):
    print "\033[33mWARNING: " + msg + "\033[0m"

def info(name, msg):
    print "\033[32m* " + name + ": " + msg + "\033[0m"

def parse_version(version):
    x = version.split(".")
    nx = []
    for e in x:
        try:
            nx.append(int(e))
        except ValueError:
            nx.append(e)
    return tuple(nx)               


def parse_dep(dependency):
    if '==' in dependency:
        op = "=="
    elif '!=' in dependency:
        op = "!="
    elif '>=' in dependency:
        op = ">="
    elif '<=' in dependency:
        op = "<="
    elif '>' in dependency:
        op = ">"
    elif '<' in dependency:
        op = '<'
    else:
        return (dependency,)
    
    name, version = dependency.split(op)
    return (name, op, parse_version(version))


def get_src_path(obj):
    srcfile = inspect.getfile(obj)
    if os.path.islink(srcfile):
        srcfile = os.readlink(srcfile)
    srcpath = os.path.dirname(srcfile)
    return srcpath

