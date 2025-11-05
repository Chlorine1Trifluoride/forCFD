import subprocess as sp
import sys
def runpip(cmd): sp.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
print("[ start ] Setting up environment for OpenFOAM automatic tasks...")
runpip("--version")
runpip("install -r requirements.txt")
if input("press any key to continue...") != None:
    sp.run([sys.executable, "auto.py"], shell=False)
