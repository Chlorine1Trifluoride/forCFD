import os
import subprocess
import shutil
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cases_root = os.path.join("..", "forCFD")
cases = []

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
        source = os.path.join(cases_root, self.name, folder, file)
        if os.path.exists(source):
            if file==None:
                shutil.rmtree(source)
            else:
                os.remove(source)
            print(f"Deleted {source}")

    def update(self, folder, file=None):
        target = os.path.join(cases_root, "CaseTemplate", folder, file)
        source = os.path.join(cases_root, self.name, folder, file)
        if os.path.exists(source) and os.path.exists(target):
            if file==None:
                shutil.copytree(source, target, dirs_exist_ok=True)
            else:
                os.copy2(source, target)
            print(f"Updated {source}")
    def forces(self):
        timelines = []
        drag_list = []
        lift_list = []
        results = []
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
        df = pd.DataFrame({
            'Time':timelines,
            "Drag": drag_arr,
            "Lift": lift_arr,
            "Drag Mean" : drag_mean,
            "Lift Mean": lift_mean
        })
        df.to_excel(f"single_forces_{self.name}.xlsx", index=False)
       
        plt.plot(df["Time"], df["Lift"], label = "Lift", color = (0.0, 0.0, 0.0, 1.0), linestyle="-", marker="")
        plt.plot(df["Time"], df["Drag"], label = "Drag", color = (0.0, 1.0, 0.0, 1.0), linestyle="-", marker="")
        plt.plot(df["Time"], df["Lift Mean"], label = "Lift Mean", color = (0.0, 1.0, 0.0, 0.4), linestyle=":", marker="")
        plt.plot(df["Time"], df["Drag Mean"], label = "Drag Mean", color = (1.0, 0.0, 0.0, 0.4), linestyle=":", marker="")
        plt.title("Lift and Drag of Human Body  [ Wind Velocity : 60m/s ]")
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

            

