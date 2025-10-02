import os
import sys
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cases_root = os.path.join ("..", "forCFD")
print()
print("|=========================================================|")
print("                  [ Select your task. ]")
print("")
print("")
print("     [  1  ]  foamRun in OpenFOAM")
print("     [  2  ]  UPDATE FILE")
print("     [  3  ]  UPDATE FOLDER")
print("     [  4  ]  DELETE FILE")
print("     [  5  ]  DELETE FOLDER")
print("     [  6  ]  foamRun postprocessing")
print("     [  7  ]  postprocessing : Graph Manufacturing Task")
print("     [ 100 ]  준수형 병신")
print("")
print()
print("|=========================================================|")
print()
print()
print()

choice =  int(input("enter the NUMBER of task you want: "))


if choice == 1:
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


elif choice ==6:

  results = []
  folders = sorted(
    [f for f in os.listdir(cases_root) if f.endswith("deg")], 
    key=lambda x: float(x.replace("deg", "").replace("m",""))
  )
  
  for folder in folders:
    lift_list = []
    drag_list = [] 
    forces = os.path.join(cases_root, folder, "postProcessing", "Forces", "0", "forces.dat")
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
        "Case": folder[1:],
        "Lift Mean": lift_mean,
        "Lift Std": lift_std,
        "Drag Mean": drag_mean,
        "Drag Std": drag_std
      })
    else:
      results.append({
        "Case": folder,
        "Lift Mean": lift_mean,
        "Lift Std": lift_std,
        "Drag Mean": drag_mean,
        "Drag Std": drag_std
      })
  df = pd.DataFrame(results)
  df.to_excel("10423정승환-CFDsimulation_Result.xlsx", index=False)  

elif choice == 7:

  df = pd.read_excel("10423정승환_CFDsimulation_result.xlsx", header=0)

  plt.plot(df["angle"], df["Lift Mean"], label = "Lift", color = (1.0, 0.0, 0.0, 1.0), linestyle="-", marker="o")
  plt.plot(df["angle"], df["Drag Mean"], label = "Drag", color = (0.0, 0.0, 1.0, 1.0), linestyle="-", marker="o")
  plt.plot(df["angle"], df["Lift Std"], label = "Lift Std", color = (0.0, 0.0, 1.0, 0.4), linestyle=":", marker="o")
  plt.plot(df["angle"], df["Drag Std"], label = "Drag Std", color = (1.0, 0.0, 0.0, 0.4), linestyle=":", marker="o")

  plt.title("Lift and Drag in Change of Angle of Human Body")
  plt.xlabel("angle        [ degree ]")
  plt.ylabel("forces       [   N    ]")
  plt.grid(True)
  plt.legend(
    loc       = "lower right",
    frameon   = True,
    edgecolor = "black",
    facecolor = "black",
    )
  
  plt.savefig("ForcesGraph.png", dpi=300, bbox_inches='tight')
  plt.show()



elif choice > 1 and choice < 6:
  foldername = input("enter your FOLDER name: ")



  if choice == 2 or choice == 4:
    filename = input("enter your FILE name: ")
    source = os.path.join(cases_root, "CaseTemplate", foldername, filename)


    if choice == 2:
      if not os.path.exists(source):
        print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

      else:
        for folder in os.listdir(cases_root):
          if folder.endswith("deg"):
            target = os.path.join(cases_root, folder, foldername, filename)
            shutil.copy2(source, target)
            print(f"Successfully Updated {filename} in {foldername} in {folder}")


    elif choice ==4:
      for folder in os.listdir(cases_root):
        if folder.endswith("deg"):
          target = os.path.join(cases_root, folder, foldername, filename)

          if os.path.exists(target):
            os.rmtree(target)
            print(f"Successfully Deleted {filename} in {foldername} in {folder}")
            
          else:
            print(f"[FATAL ERROR] SOURCE NOT FOUND: {target}")



  elif choice == 3 or choice == 5:
    if choice == 3:
      source = os.path.join(cases_root, "CaseTemplate", foldername)
      if not os.path.exists(os.path.join(cases_root, "CaseTemplate", foldername)):
        print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

      else:
        
        for folder in os.listdir(cases_root):
          if folder.endswith("deg"):
            target = os.path.join(cases_root, folder, foldername)
            shutil.copytree(source, target)
            print(f"Successfully Updated {foldername} in {folder}")


    elif choice == 5: 
      for folder in os.listdir(cases_root):
        if folder.endswith("deg"):
          target = os.path.join(cases_root, folder, foldername)

          if os.path.exists(target):
            shutil.rmtree(target)
            print(f"Successfully Deleted {foldername} in {folder}")
            
          else:
            print(f"[FATAL ERROR] FILE NOT FOUND: {target}")      



elif choice == 100:
  print("정답입니다!")


else:
  print("[INVALID CHOICE]")

print()
print()
print("Would You Try Again?")
print()
a = True
while a == True:
  ans = input("[Y/N]: ")
  if ans == "Y" or ans == "y":
    os.execv(sys.executable, ["python"] + sys.argv)
  elif ans == "N" or ans == "n":
    a = False
  elif ans == "준수형 병신":
    print("정답입니다!!!")
  else:
    print("Please Enter Either Y or N")
    a = False
