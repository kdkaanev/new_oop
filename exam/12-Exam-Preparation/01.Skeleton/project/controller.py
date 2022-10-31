from player import Player
class Controller:
    pass

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
        suplay = self.__search_suplay_bay_type(sustenance_type)
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
        
        
        

    def duel(self,first_player_name: str, second_player_name: str ):
        pass

    def next_day(self):
        pass

    def __str__(self) -> str:
        pass
    

    def __search_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __search_suplay_bay_type(self, sustenance_type):
        for indx in range(len(self.supplies), -1, -1, -1):
            suplay = self.supplies[indx]
            if suplay.__class__.__name__ == sustenance_type:
                return suplay
