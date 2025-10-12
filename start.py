import subprocess
def run(cmd):
    subprocess.run(cmd, shell=True)
print("┌────────────────────────[start.py]────────────────────────┐")
print("│             FINISH IT QUICKLY, MOTHERF**KER!             │")
print("└──────────────────────────────────────────────────────────┘")
print("  By the way...")
choice = input("  Do you have pip, MOTHERF**KER? (N/Y) : ")
if   choice.upper() == "Y":
    run("pip --version")
    run("pip install numpy==1.24.4 --prefer-binary")
    run("pip install pandas==1.5.3 --prefer-binary")
    run("pip install matplotlib==3.7.1 --prefer-binary")
    run("python auto.py")
elif choice.upper() == "N":
    run("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
    run("/c/blueCFD-Core-2024/msys64/mingw64/bin/python.exe get-pip.py")
    run("pip --version")
    run("pip install numpy==1.24.4 --prefer-binary")
    run("pip install pandas==1.5.3 --prefer-binary")
    run("pip install matplotlib==3.7.1 --prefer-binary")
    run("python auto.py")
elif len(choice) >= 2 and choice[-2:] == "병신":
    print(f"정답입니다!! {choice[:-2]}은(는) 병신입니다!!!")
    print("해당 프로그램의 발언은 제작자의 의도와 전혀 무관함을 알려드립니다.")
    print("본 프로그램에서 누군가에 대해 '병신'이라고 표현하는 것은 사용자의 입력 내용에 의하여 결정됩니다.")
    print("  ┌──────────────────[ CONGRATULATIONS!!! ]──────────────────┐")
    print("  │                   YOU GUESSED  RIGHT!!                   │")
    print("  │                YOU FOUND THE EASTER EGG!!                │")
    print('f"│      I WILL GIVE YOU {null} DOLLAR AS YOUR PRIZE!!!      │"')
    print("  └──────────────────────────────────────────────────────────┘")
else:
  print("[INVALID CHOICE]")