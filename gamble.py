import random, menu
class Game():
    def __init__(self):
        self.money = 100
        self.trial = 0
        self.money_history = []
        self.trial_history = []
        self.money_history.append(self.money)
        self.trial_history.append(self.trial)
    def menu(self):
        list = ["", f"보유 금액 : {self.money}$", f"시도 횟수 : {self.trial}회", "", "[ 1 ] 홀짝", "  성공 : 50% 수익", "  실패 : "    , "[ 2 ] 숫자 맞추기", ""]
        title = "GAMBLE"
        menu.menu(list, title)
        try: return int(input("게임 번호 선택: "))
        except: return None
    def OddEven(self):
        list = ["", ]