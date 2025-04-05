class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price

zelda = Game("젤다의 전설: 왕국의 눈물",58000)
mario = Game("마리오 원더",54000)

print(f"첫 번째 게임 = {zelda.title},"
      f"가격 = {zelda.price}")

print(f"두 번째 게임 = {mario.title},"
      f"가격 = {mario.price}")
