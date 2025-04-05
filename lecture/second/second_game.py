import uuid

class SecondGame:
    def __init__(self, title, price):
        self.id = uuid.uuid4()  # 고유 ID 생성
        self.title = title
        self.price = price

    def __repr__(self):
        return f"SecondGame(id={self.id}, title='{self.title}', price={self.price})"