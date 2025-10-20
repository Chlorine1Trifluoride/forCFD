import os
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cases_root = os.path.join("..", "forCFD")
cases = []
results = []

class Case:
    def __init__ (self, name):
        self.name=name
        if self.name.startswith ("m-"):
            self.angle = float(self.name[1:-3])
        else:
            self.angle = float(self.name[:-3])
        cases.append(self)
        print(self.name)

    def delete(self, folder, file=None):
        source = os.path.join(cases_root, self.name, folder,)
        if file ==None:
            shutil.rmtree(source)
            print(f"Deleted {source}")
        elif os.path.exists(os.path.join(source, file)):
            os.remove(source, file)
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
        timelines = []
        drag_list = []
        lift_list = []
        dat = os.path.join(cases_root, self.name, "postProcessing", "Forces", "500", "forces.dat")
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
            "Case": self.angle,
            "Lift Mean": lift_mean,
            "Lift Std": lift_std,
            "Drag Mean": drag_mean,
            "Drag Std": drag_std
        })
        df = None
        df = pd.DataFrame({
            'Time': timelines,
            "Drag": drag_arr,
            "Lift": lift_arr
        })
        df.to_excel(f"single_forces_{self.name}.xlsx", index=False)
       
        plt.plot(df["Time"], df["Lift"], label = "Lift", color = (0.0, 0.0, 0.0, 1.0), linestyle="-", marker="")
        plt.plot(df["Time"], df["Drag"], label = "Drag", color = (0.0, 1.0, 0.0, 1.0), linestyle="-", marker="")
        plt.title(f"Lift and Drag of Human Body [ angle : {self.angle}deg ] [ Wind Velocity : 60m/s ]")
        plt.xticks([])
        plt.grid(axis='x', visible=False)
        plt.xlabel("Time         [   s   ]")
        plt.ylabel("forces       [   N   ]")
        plt.grid(True)
        plt.legend(
            loc       = "lower right",
            frameon   = True,
            edgecolor = "black",
            facecolor = "white",
            )

        plt.savefig(f"single_forces_{self.name}.png", dpi=300, bbox_inches='tight')

            

