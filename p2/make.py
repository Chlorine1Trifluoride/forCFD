import os
root = os.path.join("..", "p2")
for i in range(1,61,5): os.makedirs(os.path.join(root, f"{i}mps"), exist_ok = True)
import pyfoam
pyfoam.launch()
for case in pyfoam.cases:
    case.update('0')
    case.update('constant')
    case.update('system')
    case.update(None,'foam')
    case.changeU()