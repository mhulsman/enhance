"""Module implementing loading/writing of configuration 
variables to ini file

Author: Marc Hulsman
Date: 20-feb-08"""

import ConfigParser
import string
import os
import os.path

def loadConfig(rc_path):
    """
    returns a dictionary with key's of the form
    <section>.<option> and the values 
    """
    config = {}
    if(os.path.isfile(rc_path)):    
        cp = ConfigParser.ConfigParser()
        cp.read(rc_path)
        for sec in cp.sections():
            name = string.lower(sec)
            secconfig = {}
            for opt in cp.options(sec):
                secconfig[opt] = string.strip(cp.get(sec, opt))
            config[sec] = secconfig                
    return config

def writeConfig(filename, config):
    """
    given a dictionary with key's of the form 'section.option: value'
    write() generates a list of unique section names
    creates sections based that list
    use config.set to add entries to each section
    """
    oldmask = os.umask(0000)
    cp = ConfigParser.ConfigParser()

    sections = config.keys()
    map(cp.add_section, sections)
    for sec,secconfig in config.iteritems():
        for opt, value in secconfig.iteritems():
            cp.set(sec, opt, value)
    cp.write(open(filename, "w"))
    os.umask(oldmask)

