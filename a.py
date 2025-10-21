import subprocess
import menu
try:
    def launch(cmd): 
        subprocess.run(['C:\\users\\user\\AppData\\Local\\Programs\\Python\\Python314\\python.exe', cmd], shell = False)
    print("""
    ┌───────[ PROGRAM  LAUNCHER ]───────┐
    │                                   │
    │ FINISH IT QUICKLY, MOTHERF**KER!! │
    │                                   │
    └───────────────────────────────────┘
    """)
    cmd =  input("Enter NAME of your PYTHON file: ")
    if cmd.endswith('.py'):
        launch(cmd)
    else:
        print("Enter correct file name, MOTHERF**KER!")
except: print("[오류 발생: python 실행] 이 프로세스는 윈도우 환경에서 파이썬을 설치한 상태로 진행해야 합니다.")