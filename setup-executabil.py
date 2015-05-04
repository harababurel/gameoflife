from distutils.core import setup
import py2exe, pygame, os, sys

sys.argv.append('py2exe')

"""
origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
"""

setup(
       options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
       windows = [{'script': 'main.py'}],
       zipfile = None,
       console=['main.py']
       )
