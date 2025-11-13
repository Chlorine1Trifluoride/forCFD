import subprocess, os, sys
def runpip(cmd): subprocess.run([sys.executable, "-m", "pip"] + cmd.split(), shell=False)
print("[ start ] Setting up environment for OpenFOAM automatic tasks...")
runpip("--version")
runpip("install -r requirements.txt")
if input('Press any key to continue...')!=None:
    for i in range (1,3):
        subprocess.run(os.path.join(f'p{i}','make.py'))
        with open (os.path.join(f'p{i}','menu.py'),'w') as f:
            f.write('''
def boxheader(title):
    padding = int((35-len(title))/2)
    print('┌'+'─'*padding+title+padding*'─'+'┐')
def boxcontent(string):
    print('│'+'  '+string+' '*(33-len(string))+'│')
def boxfooter():
    print("└───────────────────────────────────┘")
def box(title, list):
    boxheader(title)
    for string in list:
        boxcontent(string)
    boxfooter()
def main():
    list = [
        "",
        "",
        "I.   Case management",
        "",
        "  [  1  ]  Update FILE",
        "  [  2  ]  Update DIRECTORY",
        "",
        "  [  3  ]  Delete FILE",
        "  [  4  ]  Delete DIRECTORY",
        ''
        '  [  5  ]  initialize'
        "",
        "",
        "II.  OpenFOAM",
        "",
        "  [  6  ]  postProcessing",
        "  [  7  ]  foamRun",
        "  [  8  ]  PARALLEL foamRun",
        "",
        ""
        ]
    title = '[ AUTO  PROCESSER ]'
    box(title, list)


''')
            with open (os.path.join(f'p{i}','auto.py'),'w') as f:
                f.write('''
import check.pyfoam as pyfoam, menu
pyfoam.launch()
ans = None


menu.main()
ans =  input("enter the NUMBER of task you want: ")
choice = int(ans)


if choice > 0 and choice < 5:
  foldername = input("enter your FOLDER name: ")


  if choice == 1 or choice == 3: 
    filename = input("enter your FILE name: ")

    if choice ==   1: 
      for case in pyfoam.cases: case.update(foldername, filename)
      
    elif choice == 3: 
      for case in pyfoam.cases: case.delete(foldername, filename)


  elif choice == 2 or choice == 4:
    if choice ==   2: 
      for case in pyfoam.cases: case.update(foldername)

    elif choice == 4:  
      for case in pyfoam.cases: case.delete(foldername)

elif choice ==     5:  import make

elif choice ==     6:  pyfoam.postProcessing()

elif choice ==     7:  pyfoam.foamRun()

elif choice ==     8:  pyfoam.parallelRun()

else: print("[INVALID CHOICE]")
                        ''')