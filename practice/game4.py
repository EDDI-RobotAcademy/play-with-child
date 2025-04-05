class Game:
    def __init__(self, title, prise):
        self.title = title
        self.prise = prise

zelda = Game("젤다의 전설: 왕국의 눈물",58000)
mario = Game("마리오 원더",54000)

print(f"첫 번째 게임 = {zelda.title}",
      f"가격 = {zelda.prise}")

print(f"두번째 게임 = {mario.title}",
      f"가격 = {mario.prise}")
