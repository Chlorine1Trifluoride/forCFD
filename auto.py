import os
import subprocess
import shutil

cases_root = os.path.join ("..", "forCFD")

print("Select your task.")
print("[ 1 ] COPY   FILE")
print("[ 2 ] DELETE FILE")
print("[ 3 ] foamRun : Available in ONLY GITHUB CODESPACE")
choice =  int(input())


if choice == 3:
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


elif choice == 1 or choice == 2:
  foldername = input("enter your FOLDER name: ")
  filename = input("enter your FILE name: ")


  if choice == 1:
    source = os.path.join(cases_root, "CaseTemplate", foldername, filename)

    if not os.path.exists(source):
      print(f"[FATAL ERROR] SOURCE NOT FOUND: {source}")

    else:
      for folder in os.listdir(cases_root):
        if folder.endswith("deg"):
          target = os.path.join(cases_root, folder, foldername, filename)
          shutil.copy2(source, target)
          print(f"Successfully Copied {filename} into {folder}")


  elif choice == 2:
    for folder in os.listdir(cases_root):
      if folder.endswith("deg"):
        target = os.path.join(cases_root, folder, foldername, filename)

        if os.path.exists(target):
          os.remove(target)
          print(f"Successfully Deleted {filename} in {folder}")
          
        else:
          print(f"[FATAL ERROR] SOURCE NOT FOUND: {target}")


else:
  print("[INVALID CHOICE] Enter Either 1 or 2 or 3.")