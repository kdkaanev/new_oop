
from player import Player
class Controller:

    def __init__(self) -> None:
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_name =[]
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_name.append(player.name)
        return f'Successfully added: {", ".join(added_name)}'


    def add_supply(self, *supplyes):
        for supply in supplyes:
            self.supplies.append(supply)


    def sustain(self, player_name,sustenance_type):
        player = self.__search_player_by_name(player_name)
        indx,suplay = self.__search_suplay_bay_type(sustenance_type)
        if player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        if suplay is None:
            if sustenance_type == 'Food':
                raise Exception("There are no food supplies left!")
            elif sustenance_type == 'Drink':
                raise Exception("There are no drink supplies left!")
        if player.stamina == player.MAX_STAMINA:
            return f"{player_name} have enough stamina."
        player.stamina = min(player.stamina + suplay.energy, player.MAX_STAMINA)
        return f"{player_name} sustained successfully with {suplay.name}."
        
        

    def duel(self,first_player_name: str, second_player_name: str ):
        player1 = self.__search_player_by_name(first_player_name)
        player2 = self.__search_player_by_name(second_player_name)
        if player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."
        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."

        if player2.stamina < player2.stamina:
            player1, player2 = player2, player1

        player1_damage = player1.stamina / 2
        player2.stamina = max(player1_damage - player2.stamina, 0)
        if player2.stamina == 0:
            return f"Winner: {first_player_name}"

        player2_damage = player2.stamina / 2
        player1.stamina = max(player2_damage - player1.stamina, 0)
        if player1.stamina == 0:
            return f"Winner: {second_player_name}"

        winner = first_player_name if player1.stamina > player2.stamina else second_player_name
        return f"Winner: {winner}"


    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self) -> str:
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result.strip()
    

    def __search_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __search_suplay_bay_type(self, sustenance_type):
        for indx in range(len(self.supplies) -1, -1, -1):
            suplay = self.supplies[indx]
            if suplay.__class__.__name__ == sustenance_type:
                return (indx, suplay)
        return (-1, None)
