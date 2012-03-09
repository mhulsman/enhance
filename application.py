import copy
from tools import *

class Application(object):
    def __init__(self, name, package_manager):
        self.name = name
        self.versions = {}
        self.constrained_versions = set()
        self.constraints = ()
        self.cur_version = None
        self.state = "available"
        self.package_manager = package_manager

    def switchVersion(self, version):
        if self.cur_version is None:
            self.cur_version = version
        elif self.cur_version == version:
            if self.cur_version.state != "available":
                self.cur_version.Clean()
        else:
            self.cur_version.Clean()
            self.cur_version = version
        self.package_manager.writeConfig()            

    def setState(self, version, state):
        if not self.cur_version is None:
            assert self.cur_version == version, "Version state change for non-current version"
        self.cur_version = version
        self.state = state
        self.package_manager.writeConfig()            

    def addConstraint(self, constraint, temporary=True):
        s = copy.copy(self)
        s.constrained_versions = set([version for version in self.constrained_versions if version.match(constraint)])
        if not temporary:
            self.constraints = self.constraints + (constraint,)
        return s

    def __len__(self):
        return len(self.constrained_versions)

    def preferredVersionOrder(self, idx, update=False):
        cv = list(self.constrained_versions)
        cv.sort(key = lambda x : x.parsed_version)
        cv = cv[::-1]
        if not update and self.cur_version in self.constrained_versions:
            del cv[cv.index(self.cur_version)]
            cv.insert(0,self.cur_version)
        s = copy.copy(self)
        return cv[idx]

    def getConfig(self):
        config = {}
        if self.cur_version:
            config.update({'version': self.cur_version.version, 
                           'state': self.cur_version.state})
        elif self.state:
            config['state'] = self.state
        return config

    def processConfig(self, config):
        if 'version' in config:
            if not config['version'] in self.versions:
                warning("configuration for " + str(self.name) + " refers to unknown version: " + str(config['version']))
            else:
                self.versions[config['version']].processConfig(config)
                self.cur_version = self.versions[config['version']]
        
        self.state = config.get('state',"available")

    def addVersion(self, l, filename):
        v = l[self.name](self, filename)
        self.versions[v.version] = v
        self.constrained_versions.add(v)

    def fulfilledDeps(self, versions):
        if self.cur_version is None:
            return True
        else:
            return self.cur_version.fulfilledDeps(versions)
    
    def dependsOn(self, app):
        if self.cur_version is None:
            return False
        else:
            return self.cur_version.dependsOn(app)

    def getUsers(self):
        return [app for app in self.package_manager.apps.values() if app.dependsOn(self) and app.state == "installed"]

    def __repr__(self):
        res = ""
        if self.state == "installed":
            res += "\033[32m" + self.name + "\033[0m"
        else:   
            res += self.name
        
        res +=  " [" + ",".join([p.versionPrint() for p in self.constrained_versions]) + "]"
        return res
