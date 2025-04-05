import uuid

class SecondPlayer:
    def __init__(self, email):
        self.id = uuid.uuid4()
        self.email = email

    def __repr__(self):
        return f"SecondPlayer(id={self.id}, email='{self.email}')"