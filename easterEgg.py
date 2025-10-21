
import random
import time
import HEIL
def game():
    print("DEATH GAME STARTING...")
    x = random.randint(1, 9)
    print("한 자리 자연수 중 아무 숫자나 골라보세요")
    choice = input(">>> ")

    if len(choice) >= 2 and choice[-2:] == "병신":
        HEIL.easter(choice)
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