from package import Package
from application import Application
from config import *
from tools import *
import os
import time
#from IPython.Debugger import Tracer; debug_here = Tracer()

class PackageManager(object):
    def __init__(self, distpath):
        self.distpath = distpath
        self.mainpath = os.getcwd()
        self.srcpath = os.path.join(os.getcwd(), "src")
        self.prefixpath = os.path.join(os.getcwd(),"sys_enhance")

        self.apps = self.get_applications()
        self.loadConfig()
        self.writeConfig()
        source_env(os.path.join(os.getcwd(), "paths"))

    def getAppsByState(self, state):
        return [app for app in self.apps.values() if app.state == state]
    
    def getAppsByNames(self, appnames):
        apps = []
        for appname in appnames:
            if not appname in self.apps:
                error("unknown application: " + str(appname))
            apps.append(self.apps[appname])
        return apps

    def addConstraint(appname, constraint, temporary=True):
        if not appname in self.apps:
            error("unknown application name: " + str(appname))
        self.apps[appname].addConstraint(constraint, temporary=temporary)

    def get_applications(self):
        package_dir = os.path.join(self.distpath, 'packages')
        if not os.path.isdir(package_dir):
            error('Cannot find package directory')
        files = os.listdir(package_dir)
        files = [file for file in files if file.endswith('.py') and '-' in file]

        applications = {}
        for file in files:
            l = {}
            p = os.path.join(package_dir,file)
            execfile(p,globals(), l)
            name = file.split('-')[0]
            if not name in applications:
                applications[name] = Application(name, self)
            applications[name].addVersion(l, file)
        
        return applications

    def loadConfig(self):
        if not os.path.isfile(os.path.join(self.mainpath, 'profile.ini')):
            error("Directory not initialized. Use: enhance init <profile_name>")
        config = loadConfig(os.path.join(self.mainpath, 'profile.ini'))
        for appname, appconfig in config.iteritems():
            if appname in self.apps:
                self.apps[appname].processConfig(appconfig)
            else:
                warning("configuration refers to unknown application " + str(appname))

    def writeConfig(self):
        config = {}
        for appname, application in self.apps.iteritems():
            c = application.getConfig()
            if c:
                config[appname] = c
        writeConfig(os.path.join(self.mainpath, 'profile.ini'), config)
  

    def merge(self, appnames):
        d = DependencyInferrer(self.apps)

        merge_apps = self.getAppsByNames(appnames)
        installed_apps = self.getAppsByState("installed")

        #determine deps
        install_versions = d.process(installed_apps, merge_apps)
        
        #split in installed/noninstalled
        installed = {}
        to_install = set()
        for iv in install_versions:
            if not iv.package_name in appnames and iv.getState() == "installed" or iv.getState() == "system":
                installed[iv.package_name] = iv
            else:
                to_install.add(iv)

        #order on dependencys
        ordered_to_install = []
        while to_install:
            change = False
            for ti in list(to_install):
                if not ti.fulfilledDeps(ordered_to_install + installed.values()):
                    continue
                change = True
                ordered_to_install.append(ti)
                to_install.discard(ti)
                if ti.application.state == "installed":
                    for u in ti.application.getUsers():
                        u = u.cur_version
                        if not u in ordered_to_install and not u in to_install:
                            to_install.add(u)
                            installed.pop(u.package_name)

            assert change, "Cannot determine dependency order, cycles?"

        if not ordered_to_install:
            warning("No packages to merge")
            return

        print "\033[1m\033[34mThe following packages will be merged:\033[0m"
        for o in ordered_to_install:
            print "* " + str(o)

        print "" 
        print "\033[31mHit ctrl-c to cancel...\033[0m" 
        time.sleep(5)
        for pos, o in enumerate(ordered_to_install):
            print "\033[1m\033[34mMerging " + o.instance_name + (" [%d/%d]" % (pos + 1,len(ordered_to_install))) + "\033[0m"
            o.Merge()
        print "\033[1m\033[34mMerging complete \033[0m"
            

            
class DependencyInferrer(object):
    def __init__(self, all_apps):
        self.all_apps = all_apps

    def process(self, installed_apps, merge_apps):
        self.merge_apps = set(merge_apps)
        self.remain_stack = list(set(installed_apps) | self.merge_apps)

        self.done_stack = []
        self.stack_apps = set(self.remain_stack)
        while self.remain_stack:
            s = self.stepStack()
            while s.next() is False:
                s = self.backtrack()
            newapps = set([self.all_apps[appname] for appname in s.deps.keys()]) - self.stack_apps
            self.remain_stack = list(newapps) + self.remain_stack

        installs = [s.version for s in self.done_stack]
        return installs
        
    
    def stepStack(self):
        app = self.remain_stack[-1]
        
        deps = []
        for elem in self.done_stack:
            if app.name in elem.deps:
                deps.extend(elem.deps[app.name])
        
        s = DependencyStackElem(app, deps, app in self.merge_apps, self.remain_stack)
        
        self.remain_stack.pop()
        self.done_stack.append(s)
        return s


    def backtrack(self):
        self.done_stack.pop()
        self.remain_stack = s.oldstack
        if not self.done_stack:
            error("Cannot fulfill dependencies!")
        return self.done_stack[-1]


class DependencyStackElem(object):
    def __init__(self, app, owndeps, update, oldstack):
        self.app = app
        self.update = update
        self.oldstack = oldstack

        self.pos = -1
        self.deps = {}
        self.owndeps = owndeps

    def next(self):
        while True:
            self.pos += 1
            if self.pos >= len(self.app):
                return False
            self.version = self.app.preferredVersionOrder(self.pos,update=self.update)
            for dep in self.owndeps:
                if not self.version.match(dep):
                    continue
            break
        self.updateDependencies() 
        return self.version

    def updateDependencies(self):
        deps = self.version.getDependencies()
        for dep in deps:
            if dep[0] in self.deps:
                self.deps[dep[0]].append(dep)
            else:
                self.deps[dep[0]] = [dep]

    
