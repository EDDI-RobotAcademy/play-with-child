from lecture.first.first_game import FirstGame
from lecture.first.first_player import FirstPlayer

zelda = FirstGame("젤다의 전설", 54000)
mario = FirstGame("마리오 원더", 56000)

print(f"첫 번째 게임: {zelda.title}, 가격: {zelda.price}")
print(f"두 번째 게임: {mario.title}, 가격: {mario.price}")

player1 = FirstPlayer("아무개")

print(f"플레이어 이름: {player1.name}")