
#필수 pip 패키지 설치
import subprocess, os, sys,shutil,make
def runpip(cmd): subprocess.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
print("[ start ] Setting up e   nvironment for OpenFOAM automatic tasks...")
runpip("--version")
runpip("install -r requirements.txt")
if input('Press Enter to continue...')!=None:
    make.p1()
    make.p2()
    make.check()
    