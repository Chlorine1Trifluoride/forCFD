import os
import subprocess
import shutil

cases_root = os.path.join ("..", "forCFD")

print("[ Select your task. ]")
print("")
print("")
print("[  1  ] foamRun in OpenFOAM")
print("[  2  ] COPY   FILE")
print("[  3  ] COPY   FOLDER")
print("[  4  ] DELETE FILE")
print("[  5  ] DELETE FOLDER")
print("[ 100 ] 준수형 병신")
print("")

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

elif choice > 1 and choice < 6:
  foldername = input("enter your FOLDER name: ")
  if choice == 2 or choice == 4:
    if choice == 2:
      
      filename = input("enter your FILE name: ")
      source = os.path.join(cases_root, "CaseTemplate", foldername, filename)

      if not os.path.exists(source):
        print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

      else:
        for folder in os.listdir(cases_root):
          if folder.endswith("deg"):
            target = os.path.join(cases_root, folder, foldername, filename)
            shutil.copy2(source, target)
            print(f"Successfully Copied {filename} into {folder}")
    elif choice ==4:
      print("")

  elif choice == 3 or choice == 5:
    if choice == 3:
      filename = input("enter your FILE name: ")
      for folder in os.listdir(cases_root):
        if folder.endswith("deg"):
          target = os.path.join(cases_root, folder, foldername, filename)

          if os.path.exists(target):
            os.remove(target)
            print(f"Successfully Deleted {filename} in {folder}")
            
          else:
            print(f"[FATAL ERROR] FILE NOT FOUND: {target}")


    elif choice == 5: 

      for folder in os.listdir(cases_root):
        if folder.endswith("deg"):
          target = os.path.join(cases_root, folder, foldername)

          if os.path.exists(target):
            os.remove(target)
            print(f"Successfully Deleted {folder}")
            
          else:
            print(f"[FATAL ERROR] DIRECTORY NOT FOUND: {target}")


elif choice == 100:
  print("정답입니다!")


else:
  print("[INVALID CHOICE]")