import subprocess, os, sys
def runpip(cmd): subprocess.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
print("[ start ] Setting up environment for OpenFOAM automatic tasks...")
runpip("--version")
runpip("install -r requirements.txt")
if input('Press any key to continue...')!=None:
    for i in range (1,3):subprocess.run(os.path.join(f'p{i}','make.py'))
