class Food:
    def __init__(self,name,prise):
        self.name = name
        self.prise = prise

firstFood = Food("아이스크림",4400)
print(f"firstfood.name = {firstFood.name},firstfood.prise={firstFood.prise}")