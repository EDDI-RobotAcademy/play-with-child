import uuid

class SecondPlayerOwnedGame:
    def __init__(self, playerId, gameId):
        self.id = uuid.uuid4()
        self.playerId = playerId
        self.gameId = gameId

    def __repr__(self):
        return f"SecondPlayerOwnedGame(id={self.id}, playerId={self.playerId}, gameId={self.gameId})"