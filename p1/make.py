import os
root = os.path.join("..", "p1")
for i in range(1,61,5): 
    os.makedirs(os.path.join(root, f"{i}deg"), exist_ok = True)
import pyfoam
pyfoam.launch()
for case in pyfoam.cases:
    case.update('0')
    case.update('constant')
    case.update('system')
    case.update(None,f'{case.name}.foam')
    case.transformPoints()
    os.remove(os.path.join(root,case.name,'constant','triSurface','humaHQ0deg.stl'))