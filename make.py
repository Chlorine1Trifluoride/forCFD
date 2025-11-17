import os,shutil,foampy
def p1():
    root = os.path.join("..", "p1")
    for i in range(-175,181,5): 
        if i<0:os.makedirs(os.path.join(root, f"m{i}deg"), exist_ok = True)
        elif i>=0:os.makedirs(os.path.join(root, f"{i}deg"), exist_ok = True)
    foampy.launch_p1()
    shutil.copytree('CaseTemplate',os.path.join('p1','CaseTemplate'),dirs_exist_ok=True)
    for i in foampy.cases_p1:
        i.update('0')
        i.update('system')
        i.update('constant')
        i.update(None,'.foam')

        
def p2():
    root = os.path.join("..", "p2")
    for i in range(1,61,5): os.makedirs(os.path.join(root, f"{i}mps"), exist_ok = True)
    foampy.launch_p2()
    shutil.copytree('CaseTemplate',os.path.join('p2','CaseTemplate'),dirs_exist_ok=True)
    for i in foampy.cases_p2:
        i.update('0')
        i.update('system')
        i.update('constant')
        i.update(None,'.foam')
        i.changeU()
        with open(os.path.join(root,i,'system','controlDict'), "r") as f:
            lines = f.readlines()
        with open(os.path.join(root,i,'system','controlDict'), "w") as f:
            for line in lines:
                if "deltaT" in line:
                    f.write(f"deltaT                  0.05;\n")

def check(): shutil.copytree(os.path.join('..','CaseTemplate'), '50deg',dirs_exist_ok=True)

