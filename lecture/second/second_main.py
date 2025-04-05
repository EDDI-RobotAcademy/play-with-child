from lecture.second.second_game import SecondGame
from lecture.second.second_player import SecondPlayer
from lecture.second.second_player_owned_game import SecondPlayerOwnedGame

zelda = SecondGame("젤다의 전설: 왕국의 눈물", 58000)
mario = SecondGame("마리오 원더", 54000)
mineCraft = SecondGame("마인 크래프트", 56000)

print(f"첫 번째 게임: {zelda.title}, 가격: {zelda.price}")
print(f"두 번째 게임: {mario.title}, 가격: {mario.price}")
print(f"세 번째 게임: {mineCraft.title}, 가격: {mineCraft.price}")

changhee = SecondPlayer("infinityascent333@gmail.com")
sanghoon = SecondPlayer("gcccompil3r@gmail.com")

print(f"창희 이메일 주소: {changhee.email}")
print(f"상훈 이메일 주소: {sanghoon.email}")

playerOwnedGameList = []
playerOwnedGameList.append(SecondPlayerOwnedGame(sanghoon.id, zelda.id))
playerOwnedGameList.append(SecondPlayerOwnedGame(sanghoon.id, mario.id))
playerOwnedGameList.append(SecondPlayerOwnedGame(sanghoon.id, mineCraft.id))

playerOwnedGameList.append(SecondPlayerOwnedGame(changhee.id, mineCraft.id))

playerDictionary = {player.id: player for player in [changhee, sanghoon]}
gameDictionary = {game.id: game for game in [zelda, mario, mineCraft]}

print("\n=== 플레이어 보유 게임 목록 ===")
for pog in playerOwnedGameList:
    player = playerDictionary.get(pog.playerId)
    game = gameDictionary.get(pog.gameId)
    print(f"- {player.email} 님이 '{game.title}' 게임을 보유하고 있습니다. (가격: {game.price}원)")