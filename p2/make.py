import os
root = os.path.join("..", "p2")
for i in range(0,61,5): os.mkdir(os.path.join(root, f"{i}mps"), exists_ok = True)