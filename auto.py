try: import HEIL, easterEgg
except: pass
import pyfoam, menu
pyfoam.launch()
repeat = True
ans = None
while repeat == True:
  menu.main()
  ans =  input("enter the NUMBER of task you want: ")
  try:
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
    elif choice ==     5: pyfoam.transformPoints()
    elif choice ==     6: pyfoam.foamRun()
    elif choice ==     7: pyfoam.postProcessing()
    elif choice ==     100: print("뭐 병신아")
    else: print("[INVALID CHOICE]")
  except ValueError:
    if len(ans) >= 2 and ans[-2:] == "병신": HEIL.easter(ans)
    elif ans.startswith("HEIL"): HEIL.HITLER()
    elif ans == "game": easterEgg.game()
    else: print("[INVALID CHOICE]")

