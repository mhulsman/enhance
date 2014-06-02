import subprocess
import tarfile
import zipfile
import gzip
import bz2
import urllib2
import urlparse
import os
from os import path
from distutils.dir_util import mkpath, remove_tree
import sys
import shutil
import inspect
from urlparse import urlsplit
import re


def enter_dir(path):
    check_dir(path)
    oldpath = os.getcwd()
    os.chdir(path)
    return oldpath



def check_dir(path):
    if not os.path.isdir(path):
        assert not os.path.exists(path), "Folder: " + str(path) + " already exists as non-directory"
        mkpath(path)


def source_env(path):
    f = open(path)
    for line in f:
        line = line.strip()
        if not line.startswith('export'):
            continue
        name, value = line[6:].strip().split('=')
        value = value.replace("$" + name, os.environ.get(name,""))
        value = value.strip()
        if value.startswith('$(') and value.endswith(')'):
            value = getCommandOutput(value[2:-1])
        os.environ[name] = value.strip()

def download(url, filename=None):
    #based on stackoverflow answer
    def getFileName(url,openUrl):
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            match = re.search('filename="(?P<filename>.*)"', str(openUrl.info()))
            if match is not None:
                return match.group('filename')
            # if no filename was found above, parse it out of the final URL.
        return os.path.basename(urlsplit(openUrl.url)[2])

    try:
        u = urllib2.urlopen(urllib2.Request(url))
    except urllib2.HTTPError, e:
        error("Could not download %s, error: %s" %(str(url), str(e)))
        
        
    try:
        filename = filename or getFileName(url,u)
        meta = u.info()
        if len(meta.getheaders("Content-Length")) > 0:
            file_size = int(meta.getheaders("Content-Length")[0])
        else:
            file_size = -1

        if file_size < 0:
            file_size == "unknown"
        print "Downloading: %s Bytes: %s" % (filename, str(file_size))
        f = open(filename, 'w')
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += block_sz
            f.write(buffer)
            if file_size >= 0:
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            else:
                status = r"%10d  [file size unknown]" % (file_size_dl)
            status = status + chr(8)*(len(status)+1)
            print status,
        f.close()
    finally:
        u.close()
    return filename

def is_gzipfile(filename):
    try:
        gzip.open(filename,'r')
        gzip.close()
        return True
    except Exception:
        return False

def unpack(filename, workdir=""):
    res = []
    if not workdir:
        if filename.endswith('.tar.gz'):
            workdir = filename[:-7]
        elif filename.endswith('.tar.xz'):
            workdir = filename[:-7]
        elif filename.endswith('.tar.bz2'):
            workdir = filename[:-8]
        elif filename.endswith('.tgz') or filename.endswith('.zip'):
            workdir = filename[:-4]
        else:
            raise RuntimeError, "Cannot determine work directory"
    
    if os.path.isdir(workdir):
        remove_tree(workdir)
   
    if filename.endswith('bz2'):
        runCommand("tar -xjf " + filename)
    elif filename.endswith('zip'):
        runCommand("unzip -o " + filename)
    elif filename.endswith('.tar.xz'):
        runCommand("tar -xf " + filename)
    else:
        runCommand("tar -xzf " + filename)
    return workdir

def runCommand(cmd,exception=False):
    #print "Executing: \n" + cmd
    res = subprocess.call(cmd,shell=True)
    if not res == 0:
        if exception:
            raise RuntimeError, "Command failed"
        else:
            error('The following command failed: ' + cmd)

def getCommandOutput(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    res = p.communicate()[0]
    if p.returncode != 0:
        raise RuntimeError, "Command failed"
    return res


def platformContains(value):
    q = getCommandOutput('uname -a')
    return value in q

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
    srcpath = os.path.abspath(os.path.dirname(srcfile))
    return srcpath

def modifyEnviron(moddict):
    olddict = {}
    for k,v in moddict.iteritems():
        if k in os.environ:
            olddict[k]=  os.environ[k]
        else:
            olddict[k] = ""
        
        if v:
            os.environ[k]= v
        else:
            del os.environ[k]
            
    return olddict
