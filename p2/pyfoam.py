import os
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
cases_root = os.path.join('..', 'p2')
cases = []
casesproc = []
results = []
process = []
class Case:
    def __init__(self, name):
        try:
            self.name=name
            self.velocity = float(self.name[:-3])
            if self.velocity>0:
                casesproc.append(self)
                casesproc.sort(key = lambda case:case.velocity)
            cases.append(self)
            cases.sort(key = lambda case:case.velocity)
        except: pass
    def delete(self, folder, file=None):
        source = os.path.join(cases_root, self.name, folder,)
        if file ==None:
            shutil.rmtree(source)
            print(f"Deleted {source}")
        elif os.path.exists(os.path.join(source, file)):
            os.remove(os.path.join(source, file))
            print(f"Deleted {os.path.join(source, file)}")

    def update(self, rawfolder, file=None):
        folder = str(rawfolder)
        target = os.path.join(cases_root, "CaseTemplate", folder)
        source = os.path.join(cases_root, self.name, folder)
        if file==None and os.path.exists(target):
            shutil.copytree(target, source, dirs_exist_ok=True)
            print(f"Updated {source}")
        elif os.path.exists(os.path.join(target, file)):
            shutil.copy2(os.path.join(target, file), os.path.join(source, file) )
            print(f"Updated {os.path.join(source, file)}")
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
                timeline = line[:7].strip()
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
        results.append({
            "Case": self.velocity,
            "Lift Mean": lift_mean,
            "Lift Std": lift_std,
            "Drag Mean": drag_mean,
            "Drag Std": drag_std,
            "Gravity" : 686
        })
        df = pd.DataFrame({
            'Time': timelines,
            "Drag": drag_arr,
            "Lift": lift_arr,
            "Gravity": 686
        })
        df.to_excel(f"single_forces_{self.name}.xlsx", index=False)
       
        plt.plot(df["Time"], df["Drag"], label = "Drag", color = (0.0, 0.0, 0.0, 1.0), linestyle="-", marker="")
        plt.plot(df["Time"], df["Gravity"], label = "Gravity", color = (0.0, 0.0, 1.0, 0.7), linestyle=":", marker="")
        plt.plot(df["Time"], df["Lift"], label = "Lift", color = (0.0, 1.0, 0.0, 1.0), linestyle="-", marker="")
        plt.title(f"Lift and Drag of Human Body [ velocity : {self.velocity}deg ] [ Wind Velocity : 60m/s ]")
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

        plt.savefig(f"single_forces_{self.velocity}.png", dpi=300, bbox_inches='tight')
        timelines.clear()
        lift_list.clear()
        drag_list.clear()
        plt.close()
    
    def foamRun(self):
        try: 
            p = subprocess.Popen(["foamRun"], cwd = os.path.join(cases_root, self.name))
            return p
        except: print("[오류 발생: foamRun] 이 프로세스는 v11 이상의 OpenFOAM 환경에서 진행해야 합니다.")
    def transformPoints(self):
        try:
            command = f"transformPoints 'Rx={self.velocity}' "
            p = subprocess.Popen(command, cwd = os.path.join(cases_root, self.name), shell=True)
            return p
        except: print("[오류 발생: foamRun] 이 프로세스는 v11 이상의 OpenFOAM 환경에서 진행해야 합니다.")

def postProcessing():
    global results
    results.clear()
    folders = sorted(cases, key = lambda f:f.velocity )
    for case in folders: case.forces()
    df = pd.DataFrame(results)
    df.to_excel("total_forces_10423.xlsx", index=False)
    plt.plot(df["Case"], df["Drag Std"], label = "Drag Std", color = (0.0, 0.0, 0.0, 0.4), linestyle=":", marker="")
    plt.plot(df["Case"], df["Lift Std"], label = "Lift Std", color = (0.0, 1.0, 0.0, 0.4), linestyle=":", marker="")
    plt.plot(df["Case"], df["Drag Mean"], label = "Drag", color = (0.0, 0.0, 0.0, 1.0), linestyle="-", marker="")
    plt.plot(df["Time"], df["Gravity"], label = "Gravity", color = (0.0, 0.0, 1.0, 0.7), linestyle=":", marker="")
    plt.plot(df["Case"], df["Lift Mean"], label = "Lift", color = (0.0, 1.0, 0.0, 1.0), linestyle="-", marker="")
    plt.title(f"Lift and Drag of Human Body [ velocity : [ Wind Velocity : 60m/s ]")
    plt.xlabel("velocity        [  deg  ]")
    plt.ylabel("Force        [   N   ]")
    plt.grid(True)
    plt.legend(
        loc       = "lower right",
        frameon   = True,
        edgecolor = "black",
        facecolor = "white",
        )

    plt.savefig(f"total_forces_10423.png", dpi=300, bbox_inches='tight')
    plt.close()

def launch(): 
    cases.clear()
    for case in os.listdir(cases_root): case = Case(case)

def conc(func):
    def wrapper():
        global process
        process = []
        num = int(input("Concurrency level: "))
        for i in range(0, len(casesproc), num):
            batch = casesproc[i : i+num]
            for case in batch:
                p = func(case)
                if p: process.append(p)
            for p in process: p.wait()
            process.clear()
    return wrapper
@conc
def foamRun(case): return case.foamRun()
@conc
def transformPoints(case): return case.transformPoints()