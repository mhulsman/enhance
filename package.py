from tools import *
import shutil

class Package(object):
    def __init__(self, application, filename):
        self.application = application
        self.parseFilename(filename)
        assert self.package_name == self.application.name, "Mismatch in application name and package name"
        self.state = "available"
    
        self.prefixpath = self.application.package_manager.prefixpath
        self.srcpath = self.application.package_manager.srcpath
        self.mainpath = self.application.package_manager.mainpath
        self.distpath = self.application.package_manager.distpath

    def processConfig(self, config):
        self.state = config.get('state', "available")

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        self.application.setState(self, state)

    def parseFilename(self, filename):
        if filename.endswith('.py'):
            filename = filename[:-3]
       
        name,version = filename.split('-')
        if not hasattr(self, 'instance_name'):
            self.instance_name = filename

        if not hasattr(self, 'package_name'):
            self.package_name = name

        if not hasattr(self, 'version'):
            self.version = version

        if not hasattr(self, 'parsed_version'):            
            self.parsed_version = parse_version(self.version)

    def fillVars(self, cmd, **kwargs):
        vars = {'full_name':self.instance_name, 
                'name':self.package_name, 
                'version':self.version,
                'prefix':self.prefixpath,
                'srcpath':self.srcpath,
                'rootpath':self.mainpath,
                'distpath':self.distpath}
        vars.update(kwargs)
        return cmd % vars

    def Merge(self):
        self.application.switchVersion(self)
        
        info(self.instance_name, "Starting merge")

        oldpath = enter_dir(self.srcpath)

        if hasattr(self,'workdir'):
            if os.path.isdir(self.workdir):
                shutil.rmtree(self.workdir)
                

        package_file = self.Fetch()

        workdir = self.Unpack(package_file)

        if workdir:
            workdir = self.fillVars(workdir)
            enter_dir(workdir)

        self.Config()

        self.Build()

        self.Install()

        os.chdir(oldpath)
        info(self.instance_name, "Merge finished")

    def Clean(self):
        info(self.instance_name, "clean")
        self.setState("available")

    def Fetch(self):
        if hasattr(self,"fetch"):
            info(self.instance_name, "fetch")
            if not isinstance(self.fetch,str):
                self.package_file = self.fetch()
            else: 
                self.package_file = download(self.fillVars(self.fetch))
            return self.package_file
        return ""            

    def Unpack(self, package_file):
        workdir = getattr(self,"workdir","")
        if package_file:
            info(self.instance_name, "unpack")
            if not hasattr(self, "unpack"):
                workdir = unpack(package_file, workdir)
            else:
                workdir = self.unpack(package_file, workdir)
            if not hasattr(self, "workdir"):
                self.workdir = workdir
        return workdir
        
    def Config(self):        
        if hasattr(self, 'config'):
            info(self.instance_name, "config")
            if isinstance(self.config, str):
                runCommand(self.fillVars(self.config))
            else:
                self.config(prefixpath)

    def Build(self):
        if hasattr(self, 'build'):
            info(self.instance_name, "build")
            if isinstance(self.build, str):
                runCommand(self.fillVars(self.build))
            else:
                self.build(prefixpath)

    def Install(self):
        if hasattr(self, 'install'):
            info(self.instance_name, "install")
            if isinstance(self.install, str):
                runCommand(self.fillVars(self.install))
            else:
                self.install(prefixpath)
        self.setState("installed")
    
    def getDependencies(self):
        if not hasattr(self, 'dependencies'):
            return []
        if not hasattr(self, 'parsed_dependencies'):            
            self.parsed_dependencies = tuple([parse_dep(dependency) for dependency in self.dependencies])
        return self.parsed_dependencies


    def dependsOn(self, app):
        for dep in self.getDependencies():
            if dep[0] == app.name:
                return True
        return False

    def fulfilledDeps(self, versions):
        deps = self.getDependencies()
        versions = dict([(v.package_name,v) for v in versions])
        for dep in deps:
            if not dep[0] in versions:
                return False
            if not versions[dep[0]].match(dep):
                return False
        return True

    def match(self, constraint):
        if len(constraint) == 1:
            return constraint[0] == self.package_name

        name, op, version = constraint
        if not name == self.package_name:
            return False
        if op == "==":
            return self.parsed_version == version
        elif op == '!=':
            return self.parsed_version != version
        elif op == '>=':
            return self.parsed_version >= version
        elif op == '<=':
            return self.parsed_version <= version
        elif op == '<':
            return self.parsed_version < version
        elif op == '>':
            return self.parsed_version > version
        raise RuntimeError, "Unknown op: " + str(op)

    def versionPrint(self):
        if self.state == "installed":
            return "\033[35m" + self.version + "\033[0m"
        elif self.state == "system":
            return "\033[33m" + self.version + "\033[0m"
        else:
            return "\033[36m" + self.version + "\033[0m"

    def __repr__(self):
        if self.state == "installed":
            return "\033[35m" + self.instance_name + "\033[0m"
        elif self.application.state == "installed":
            return "\033[33m" + self.instance_name + "\033[0m"
        else:
            return "\033[32m" + self.instance_name + "\033[0m"


class MakePackage(Package):
    config="./configure --prefix=%(prefix)s"

    build="make"

    install="make install"

class PythonPackage(Package):
    dependencies=["python"]

    install="python setup.py install --prefix=%(prefix)s"

class EasyInstallPackage(Package):
    dependencies = ["setuptools"]
    workdir="%(prefix)s"
    install="easy_install %(name)s"
