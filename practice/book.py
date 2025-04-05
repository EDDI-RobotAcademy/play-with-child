class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

firstBook = Book("스타크래프트 대망의 전설1",300000)
print(f"firstBook.name = {firstBook.name}, price = {firstBook.price}")