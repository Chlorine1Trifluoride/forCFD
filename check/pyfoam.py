import os
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
cases_root=os.path.join('..', 'forCFD')
cases=[];casesproc=[];process=[];results=[]
r_case=[]; r_lift_mean=[]; r_lift_std=[]; r_drag_mean=[]; r_drag_std=[]
class Case:
    def __init__(self, name):
        try:
            self.name=name
            self.angle = float(self.name[:-3])
            cases.append(self)
        except: pass
    def delete(self, folder, file=None):
        source = os.path.join(cases_root, self.name, folder,)
        if file ==None:
            shutil.rmtree(source)
            print(f"Deleted {source}")
        elif os.path.exists(os.path.join(source, file)):
            os.remove(os.path.join(source, file))
            print(f"Deleted {os.path.join(source, file)}")
    def forces(self):
        global results
        timelines = []
        drag_list = []
        lift_list = []
        dat = os.path.join(cases_root, self.name, "postProcessing", "Forces", "0", "forces.dat")
        with open(dat, "r")as f:
            for line in f:
                if line.startswith("#") or line.strip() =="":
                    continue
                timeline = float(line[:4].strip())
                if timeline<1.3:continue
                vectors = re.findall(r"\(([^()]+)\)", line)
                f_a = vectors[0].strip().split()
                f_b = vectors[1].strip().split()
                lift = float(f_a[2]) + float(f_b[2])
                drag = float(f_a[1]) + float(f_b[1])
                drag_list.append(drag)
                lift_list.append(lift)
                timelines.append(timeline)
        drag_arr = np.array(drag_list)
        lift_arr = np.array(lift_list)
        drag_mean = np.mean(drag_arr)
        lift_mean = np.mean(lift_arr)
        drag_std = np.std(drag_arr)
        lift_std = np.std(lift_arr)
        timelines_arr = np.array(timelines)
        r_case.append(self.angle)
        r_lift_mean.append(lift_mean)
        r_lift_std.append(lift_std)
        r_drag_mean.append(drag_mean)
        r_drag_std.append(drag_std)
        results.append({
            "Case": self.angle,
            "Lift Mean": lift_mean,
            "Lift Std": lift_std,
            "Drag Mean": drag_mean,
            "Drag Std": drag_std,
        })
        df = pd.DataFrame({
            "Time": timelines_arr,
            "Drag": drag_arr,
            "Lift": lift_arr,
        })

        df.to_excel(f"single_forces_{self.name}.xlsx", index=False)

        plt.plot(timelines_arr, drag_arr, label = "Drag", color = (0.0, 0.0, 0.0, 0.5), linestyle="-", marker="")
        plt.axhline(y=float(686), label = "Gravity", color = (0.0, 0.0, 1.0, 0.7), linestyle=":")
        plt.plot(timelines_arr, lift_arr, label = "Lift", color = (1.0, 0.0, 0.0, 1.0), linestyle="-", marker="")

        plt.title(f"Lift and Drag of Human Body [ angle : {self.angle}deg ] [ Wind Velocity : 60m/s ]")
        plt.xticks([])
        plt.grid(axis='x', visible=False)
        plt.xlabel("Time         [   s   ]")
        plt.ylabel("Force        [   N   ]")
        plt.grid(True)
        plt.legend(
            loc       = "lower right",
            frameon   = True,
            edgecolor = "black",
            facecolor = "white",
            )

        plt.savefig(f"single_forces_{self.angle}.png", dpi=300, bbox_inches='tight')
        timelines.clear()
        lift_list.clear()
        drag_list.clear()
        plt.close()
    
    def decompose(self, num):
        with open (os.path.join(cases_root,self.name,"system","decomposeParDict"), "r") as f:
            lines = f.readlines()
        with open (os.path.join(cases_root,self.name,"system","decomposeParDict"), "w") as f:
            for line in lines:
                if "numberOfSubdomains" in line:
                    f.write(f"numberOfSubdomains  {num};\n")
                else:f.write(line)
        try: 
            subprocess.run(["decomposePar"], cwd = os.path.join(cases_root, self.name))
        except: print("[오류 발생: foamRun] 이 프로세스는 v11 이상의 OpenFOAM 환경에서 진행해야 합니다.")
        subprocess.Popen(["mpirun","-np",str(num),"foamRun","-parallel"], cwd = os.path.join(cases_root,self.name))

    def foamRun(self):
        try: 
            p = subprocess.Popen(["foamRun"], cwd = os.path.join(cases_root, self.name))
            return p
        except: print("[오류 발생: foamRun] 이 프로세스는 v11 이상의 OpenFOAM 환경에서 진행해야 합니다.")
    def transformPoints(self):
        try:
            command = f"transformPoints 'Rx={self.angle}' "
            p = subprocess.Popen(command, cwd = os.path.join(cases_root, self.name), shell=True)
            return p
        except: print("[오류 발생: foamRun] 이 프로세스는 v11 이상의 OpenFOAM 환경에서 진행해야 합니다.")

def launch(): 
    cases.clear()
    for case in os.listdir(cases_root): case = Case(case)
def foamRun():
    for case in cases:case.foamRun()
def transformPoints():
    for case in cases:case.transformPoints()
def parallelRun():
    num = input("Enter Number of Subdomains: ")
    for case in cases:case.decompose(num)
def postProcessing():
    for case in cases:case.forces()