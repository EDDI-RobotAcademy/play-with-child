class Game:
    def __init__(self,name,price):
        self.name = name
        self.price = price

game1 = Game("전투기 스타2 + 스타락타 전투기",92391)
game2 = Game ("슈퍼 마리오 스타 리드 캉캉캉",49462)

print(f"game1.name = {game1.name},"
      f"game1.price = {game1.price}")

print(f"game2.name = {game2.name},"
      f"game2.price = {game2.price}")
