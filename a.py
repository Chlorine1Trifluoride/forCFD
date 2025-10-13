import subprocess

def launch(cmd): 
    subprocess.run(['C:\\users\\user\\AppData\\Local\\Programs\\Python\\Python314\\python.exe', cmd], shell = False)
print("""
┌────────────────────[PROGRAM LAUNCHER]────────────────────┐
│                                                          │
│             FINISH IT QUICKLY, MOTHERF**KER!             │
│                                                          │
└──────────────────────────────────────────────────────────┘
""")
cmd =  input("Enter NAME of your PYTHON file: ")
if cmd.endswith('.py'):
    launch(cmd)
else:
    print("Enter correct file name, MOTHERF**KER!")