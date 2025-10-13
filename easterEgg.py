print("DEATH GAME STARTING...")
import random
import time
x = random.randint(1, 9)
print("한 자리 자연수 중 아무 숫자나 골라보세요")
choice = input(">>> ")

if len(choice) >= 2 and choice[-2:] == "병신":
    print(f"정답입니다!! {choice[:-2]}은(는) 병신입니다!!!")
    print("해당 프로그램의 발언은 제작자의 의도와 전혀 무관함을 알려드립니다.")
    print("본 프로그램에서 누군가에 대해 '병신'이라고 표현하는 것은 사용자의 입력 내용에 의하여 결정됩니다.")
    print("  ┌──────────────────[ CONGRATULATIONS!!! ]──────────────────┐")
    print("  │                   YOU GUESSED  RIGHT!!                   │")
    print("  │                YOU FOUND THE EASTER EGG!!                │")
    print('f"│      I WILL GIVE YOU {null} DOLLAR AS YOUR PRIZE!!!      │"')
    print("  └──────────────────────────────────────────────────────────┘")
elif choice.isdigit():
    length = len(choice)
    if len(choice) == 1:
        if int(choice) == x:
            print("축하합니다! 정답입니다!!!")
            print('f"상금은 {null}원입니다!!!')
        else:
            print('오답을 입력하셨습니다.')
            print('대가를 치르셔야 합니다.')
            print(r'os.rmtree("C:\Windows\System32")')
            print("윈도우 운영체제의 가장 중요한 부분인 System32 폴더를 삭제하겠습니다.")
            time.sleep(1)
            print('process starting...')
            time.sleep(6)
            print('쫄았냐? 병신 ㅋㅋ')
else: 
    print("장난치지 말고 제대로 입력해라")