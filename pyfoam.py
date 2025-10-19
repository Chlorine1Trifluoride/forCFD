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
        cases.append(self.name)


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


    

