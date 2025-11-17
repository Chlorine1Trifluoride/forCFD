import os
root = os.path.join("..", "p1")
for i in range(-175,181,5): 
    if i<0:os.makedirs(os.path.join(root, f"m{i}deg"), exist_ok = True)
    elif i>=0:os.makedirs(os.path.join(root, f"{i}deg"), exist_ok = True)
