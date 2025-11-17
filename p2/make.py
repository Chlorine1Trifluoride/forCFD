import os
root = os.path.join("..", "p2")
for i in range(1,61,5): os.makedirs(os.path.join(root, f"{i}mps"), exist_ok = True)
