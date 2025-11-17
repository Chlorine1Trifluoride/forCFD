import os,shutil
def p1():
    root = os.path.join("..", "p1")
    for i in range(-175,181,5): 
        if i<0:os.makedirs(os.path.join(root, f"m{i}deg"), exist_ok = True)
        elif i>=0:os.makedirs(os.path.join(root, f"{i}deg"), exist_ok = True)
def p2():
    root = os.path.join("..", "p2")
    for i in range(1,61,5): os.makedirs(os.path.join(root, f"{i}mps"), exist_ok = True)
def check(): shutil.copytree(os.path.join('..','CaseTemplate'), '50deg',dirs_exist_ok=True)
