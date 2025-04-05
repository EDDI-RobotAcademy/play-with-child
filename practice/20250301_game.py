class Game:
    def __init__(self, title , price, sound):


         self.title = title
         self.price = price
         self.sound = sound

zelda = Game("젤다의 전설,왕국의 눈물",56000,""
                                   "")
mario = Game("마리오 원더",54000)



print(f"title = {zelda.title},  price = {zelda.price}")
print(f"title = {mario.title},  price = {mario.price}")