from toolz import first

class Game:
    def __init__(self,weapon,price):
        self.weapon = weapon
        self.price = price



weapon1 = Game("쉐도비의 칼날 무한  대미지",9999999999999)
weapon2 = Game ("죽음의 칼날이  사람을  죽인다  그리고  쉐도우볼도  사람을 죽인다",1)

print(f"weapon1.weapon = {weapon1.weapon},"
      f"weapon1.subject = {weapon1.price}")

print(f"weapon2.weapon = {weapon2.weapon},"
      f"weapon2.subject = {weapon2.price}")




