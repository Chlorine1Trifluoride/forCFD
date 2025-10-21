import subprocess as sp
import sys
def runpip(cmd):
    sp.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
try:
    import HEIL, menu
    menu.box("[start]", [])
except: print("[start]")
runpip("--version")
runpip("install -r requirements.txt")
sp.run([sys.executable, "auto.py"], shell=False)
