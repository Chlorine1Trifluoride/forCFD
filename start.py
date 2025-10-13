import subprocess as sp
import sys
def runpip(cmd):
    sp.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
print("┌────────────────────────[start.py]────────────────────────┐")
print("│             FINISH IT QUICKLY, MOTHERF**KER!             │")
print("└──────────────────────────────────────────────────────────┘")
runpip("--version")
runpip("install numpy")
runpip("install pandas")
runpip("install matplotlib")
sp.run([sys.executable, "auto.py"], shell=False)
