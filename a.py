import subprocess

def launch(cmd): 
    subprocess.run(['C:\users\user\AppData\Local\Programs\Python\Python311\python.exe', cmd], shell = False)
print()
print("┌────────────────────[PROGRAM LAUNCHER]────────────────────┐")
print("│                                                          │")
print("│             FINISH IT QUICKLY, MOTHERF**KER!             │")
print("│                                                          │")
print("└──────────────────────────────────────────────────────────┘")
cmd =  input("Enter NAME of your PYTHON file: ")
if cmd.endswith('.py'):
    launch(cmd)
else:
    print("Enter correct file name, MOTHERF**KER!")