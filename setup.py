#!/usr/bin/python
# vim:ts=4:sw=4:softtabstop=0:smarttab
# 
#    Copyright (C) 1999-2007  Keith Dart <keith@kdart.com>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.

"""
Master builder (custom script).

Commands:
 publish
 build
 install
 eggs
 rpms
 msis
 wininst
 develop
 clean
 squash
 eggs
 list

Most regular setuptools commands also work.

NOTE: install requires sudo to be configured for you.

"""

import sys
import os

try:
    WEXITSTATUS = os.WEXITSTATUS
except AttributeError: # running on Windows
    def WEXITSTATUS(arg):
        return arg
    os.environ["HOME"] = os.environ["USERPROFILE"]
    RSYNCCHECK = "rsync --version >nul"
else:
    RSYNCCHECK = "rsync --version >/dev/null"

PACKAGES = [
"aid",
"utils",
"core",
"CLI",
"debugger",
"process",
"SMI",
"mibs",
"SNMP",
"storage",
"QA",
"net",
"audio",
"XML",
"WWW",
"vim",
"fepy",
]

SQUASHDIR = os.environ.get("SQUASHDIR", 
        os.path.expandvars("$HOME/.local/lib/python%s/site-packages" % (sys.version[:3],)))

def _do_commands(name, cmds, root):
    # use sudo on Linux and possibly other platforms. On Windows it's
    # assumed you're running as Administrator (everybody does it...)
    if root and sys.platform not in ("win32", "cli"):
        sudo = "sudo "
    else:
        sudo = ""
    cmd = "%s%s setup.py %s" % (sudo, sys.executable, " ".join(cmds))
    print "========", name, "==", cmd
    os.chdir(name)
    try:
        rv = WEXITSTATUS(os.system(cmd)) == 0
    finally:
        os.chdir("..")
        print "====================== END", name
        print
    return rv

def do_eggs(name):
    return _do_commands(name, ["bdist_egg"], False)

def do_rpms(name):
    return _do_commands(name, ["bdist_rpm"], False)

def do_msis(name):
    return _do_commands(name, ["bdist_msi"], False)

def do_wininst(name):
    return _do_commands(name, ["bdist_wininst"], False)

def do_develop(name):
    return _do_commands(name, ["develop -s $HOME/bin -l -N"], False)

def do_publish(name):
    return _do_commands(name, ['egg_info -RDb ""', "sdist", "register", "upload"], False)

def do_egg_info(name):
    return _do_commands(name, ['egg_info'], False)

def do_install(name):
    return _do_commands(name, ["install -O2"], True)

def do_clean(name):
    return _do_commands(name, ["clean"], False)

def do_list(name):
    print name,
    return True

# "squash" selected sub packages to a single package. Also removes
# setuptools dependency when tarballed.
def do_squash(name):
    if not _check_rsync():
        print "Squash requires rsync tool to be installed."
        return False
    if not os.path.isdir(SQUASHDIR):
        os.mkdir(SQUASHDIR)
    os.chdir(name)
    uname = os.uname()
    bin_dir = ps.path.join("build", "lib.%s-%s-%s" % (uname[0].lower(), uname[4], sys.version[:3]))
    # e.g: build/lib.linux-x86_64-2.5/pycopia
    print "======== SQUASH", name, "to", SQUASHDIR
    try:
        if WEXITSTATUS(os.system("%s setup.py build" % (sys.executable,))) != 0:
            return False
        for pydir in ("build/lib", bin_dir):
            if os.path.isdir(pydir):
                cmd = "rsync -azvu %s/ %s" % (pydir, SQUASHDIR)
                if WEXITSTATUS(os.system(cmd)) != 0:
                    return False
    finally:
        os.chdir("..")
    _null_init(SQUASHDIR)
    print "====================== END", name, "squashed into", SQUASHDIR
    print
    return True

def _null_init(directory):
    open(os.path.join(directory, "pycopia", "__init__.py"), "w").close()

def _check_rsync():
    return WEXITSTATUS(os.system(RSYNCCHECK)) == 0

def do_generic(name):
    pass

def main(argv):
    try:
        cmd = argv[1]
    except IndexError:
        print __doc__
        return 1
    try:
        meth = globals()["do_" + cmd]
    except KeyError:
        def meth(name):
            return _do_commands(name, [cmd], False)
    for name in (argv[2:] or PACKAGES):
        if not meth(name):
            break
    print
    return 0

sys.exit(main(sys.argv))
