from controller import Controller
from player import Player


player = Player('putjo', 25, 17)
player2 = Player('putjo1', 23, 34)
controller = Controller()
print(controller.add_player(player, player2))

