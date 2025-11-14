import os,shutil,pyfoam
shutil.copytree(os.path.join('..','CaseTemplate'), '50deg',dirs_exist_ok=True)
pyfoam.launch()
pyfoam.transformPoints()