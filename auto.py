import os
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import colorama

cases_root = os.path.join ("..", "forCFD")


'''
작업별 프로세스 스크립트
'''
def foamRun():
  case = []
  for folder in os.listdir(cases_root):
    if folder.endswith("deg"):
      case.append(folder)
      print(f"System found {folder}")
  for i in range(0, len(case), 3):
    batch = case[ i : i+3 ]
    process = []
    for folder in batch:
      p = subprocess.Popen(["foamRun"], cwd = os.path.join(cases_root, folder))
      process.append(p)
    for p in process:
      p.wait()

def totalexcel(): 
  results = []
  folders = sorted(
    [f for f in os.listdir(cases_root) if f.endswith("deg")], 
    key=lambda x: float(x.replace("deg", "").replace("m",""))
  )
  
  for folder in folders:
    lift_list = []
    drag_list = [] 
    forces = os.path.join(cases_root, folder, "postProcessing", "Forces", "500", "forces.dat")
    with open(forces, "r") as f:
      for line in f:
        if line.startswith("#") or line.strip() == "":
          continue
        vectors = re.findall(r"\(([^()]+)\)", line)
        f_a = vectors[0].strip().split()
        f_b = vectors[1].strip().split()
        drag = float(f_a[1])+float(f_b[1])
        lift = float(f_a[2])+float(f_b[2])
        drag_list.append(drag)
        lift_list.append(lift)
    drag_arr = np.array(drag_list)
    lift_arr = np.array(lift_list)
    drag_mean = np.mean(drag_arr)
    lift_mean = np.mean(lift_arr)
    drag_std = np.std(drag_arr)
    lift_std = np.std(lift_arr)
    if folder.startswith("m"):
      results.append({
        "Case": float(folder[1:-3]),
        "Lift Mean": lift_mean,
        "Lift Std": lift_std,
        "Drag Mean": drag_mean,
        "Drag Std": drag_std
      })
    else:
      results.append({
        "Case": float(folder[:-3]),
        "Lift Mean": lift_mean,
        "Lift Std": lift_std,
        "Drag Mean": drag_mean,
        "Drag Std": drag_std
      })
  df = pd.DataFrame(results)
  df.to_excel("10423정승환-CFDsimulation_Result.xlsx", index=False) 

def transformPoints():
  case = []
  for folder in os.listdir(cases_root):
    if folder.endswith("deg"):
      case.append(folder)
      print(f"System found {folder}")
  for i in range(0, len(case), 9):
    batch = case[ i : i+9 ]
    process = []
    for folder in batch:
      if folder.startswith("m"):
        angle = float(folder[1:-3])
      else:
        angle = float(folder[:-3])
      command = f" transformPoints 'Rx={angle}' "
      p = subprocess.Popen(command, cwd = os.path.join(cases_root, folder), shell=True)
      process.append(p)
    for p in process:
      p.wait()

def totalgraph():
  df = pd.read_excel("10423정승환-CFDsimulation_Result.xlsx", header=0)
  df["angle"] = df["Case"]

  plt.plot(df["angle"], df["Lift Mean"], label = "Lift", color = (0.0, 0.0, 0.0, 1.0), linestyle="-", marker="")
  plt.plot(df["angle"], df["Drag Mean"], label = "Drag", color = (0.0, 1.0, 0.0, 1.0), linestyle="-", marker="")
  plt.plot(df["angle"], df["Lift Std"], label = "Lift Std", color = (0.0, 1.0, 0.0, 0.4), linestyle=":", marker="")
  plt.plot(df["angle"], df["Drag Std"], label = "Drag Std", color = (1.0, 0.0, 0.0, 0.4), linestyle=":", marker="")
  plt.title("Lift and Drag of Human Body  [ Wind Velocity : 60m/s ]")
  plt.xlabel("angle        [ degree ]")
  plt.ylabel("forces       [   N    ]")
  plt.grid(True)
  plt.legend(
    loc       = "lower right",
    frameon   = True,
    edgecolor = "black",
    facecolor = "white",
    )

  plt.savefig("ForcesGraph.png", dpi=300, bbox_inches='tight')
  plt.show()

def updatefile(foldername, filename):
  source = os.path.join(cases_root, "CaseTemplate", foldername, filename)
  if not os.path.exists(source):
    print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

  else:
    for folder in os.listdir(cases_root):
      if folder.endswith("deg"):
        target = os.path.join(cases_root, folder, foldername, filename)
        shutil.copy2(source, target)
        print(f"Successfully Updated {filename} in {foldername} in {folder}")

def deletefile(foldername, filename):
  for folder in os.listdir(cases_root):
    if folder.endswith("deg"):
      target = os.path.join(cases_root, folder, foldername, filename)

      if os.path.exists(target):
        os.remove(target)
        print(f"Successfully Deleted {filename} in {foldername} in {folder}")
        
      else:
        print(f"[FATAL ERROR] SOURCE NOT FOUND: {target}")

def updatefolder(foldername):
  source = os.path.join(cases_root, "CaseTemplate", foldername)
  if not os.path.exists(os.path.join(cases_root, "CaseTemplate", foldername)):
    print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

  else:
    
    for folder in os.listdir(cases_root):
      if folder.endswith("deg"):
        target = os.path.join(cases_root, folder, foldername)
        shutil.copytree(source, target, dirs_exist_ok=True)
        print(f"Successfully Updated {foldername} in {folder}")

def deletefolder(foldername):
  for folder in os.listdir(cases_root):
    if folder.endswith("deg"):
      target = os.path.join(cases_root, folder, foldername)

      if os.path.exists(target):
        shutil.rmtree(target)
        print(f"Successfully Deleted {foldername} in {folder}")
        
      else:
        print(f"[FATAL ERROR] FILE NOT FOUND: {target}")

        
repeat = True
while repeat == True:
  print("""
  ┌─────────────────────[AUTO PROCESSER]─────────────────────┐
  │                                                          │
  │             FINISH IT QUICKLY, MOTHERF**KER!             │
  │                                                          │
  │                                                          │
  │   I.   Case management                                   │
  │                                                          │
  │    [  1  ]  Update FILE                                  │
  │    [  2  ]  Update DIRECTORY                             │
  │                                                          │
  │    [  3  ]  Delete FILE                                  │
  │    [  4  ]  Delete DIRECTORY                             │
  │                                                          │
  │                                                          │
  │   II.  OpenFOAM                                          │
  │                                                          │
  │    [  5  ]  transformPoints                              │
  │    [  6  ]  foamRun                                      │
  │                                                          │
  │                                                          │
  │   III. PostProcessing                                    │
  │                                                          │
  │    [  7  ]  TOTAL    Excel                               │
  │    [  8  ]  TOTAL    Graph                               │
  │                                                          │
  │    [  9  ]  SPECIFIC Excel                               │
  │    [  10 ]  SPECIFIC Graph                               │
  │                                                          │
  │                                                          │
  └──────────────────────────────────────────────────────────┘
  """)
  ans =  input("enter the NUMBER of task you want: ")
  
  try:
    choice = int(ans)
    if choice == 1:
      foamRun()

    elif choice ==6:
      totalexcel()

    elif choice == 7:
      totalgraph()

    elif choice == 8:
      transformPoints()


    elif choice > 0 and choice < 5:
      foldername = input("enter your FOLDER name: ")

      if choice == 2 or choice == 4:
        filename = input("enter your FILE name: ")
        source = os.path.join(cases_root, "CaseTemplate", foldername, filename)

        if choice == 2:
          updatefile(foldername, filename)

        elif choice ==4:
          deletefile(foldername, filename)

      elif choice == 3 or choice == 5:
        if choice == 3:
          updatefolder(foldername)

        elif choice == 5: 
          deletefolder(foldername)


    elif choice == 100:
      print("뭐 병신아")

  except ValueError:
    if len(ans) >= 2 and ans[-2:] == "병신":
        print(f"정답입니다!! {ans[:-2]}은(는) 병신입니다!!!")
        print(r'''
        해당 프로그램의 발언은 제작자의 의도와 전혀 무관함을 알려드립니다.
        본 프로그램에서 누군가에 대해 '병신'이라고 표현하는 것은 사용자의 입력 내용에 의하여 결정됩니다.
          ┌──────────────────[ CONGRATULATIONS!!! ]──────────────────┐
          │                   YOU GUESSED  RIGHT!!                   │
          │                YOU FOUND THE EASTER EGG!!                │
        f"│      I WILL GIVE YOU {null} DOLLAR AS YOUR PRIZE!!!      │"
          └──────────────────────────────────────────────────────────┘
          ''')

    else:
      print("[INVALID CHOICE]")

