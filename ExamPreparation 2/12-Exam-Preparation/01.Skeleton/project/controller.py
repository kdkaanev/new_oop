from project.supply.drink import Drink
from project.supply.food import Food
from project import supply

from project.player import Player
from supply import food, drink
from supply.supply import Supply


class Controller:
    NO_FOOD_ERROR_MESSAGE = "There are no food supplies left!"
    NO_DRINK_ERROR_MESSAGE = "There are no drink supplies left!"

    def __init__(self):
        self.players = []
        self.supplies = []
        self.player_by_player_names = {}

    def add_player(self, *args):
        """
        Add the players to the 'players'.
         - if player exist:-don't add
•       return a message with the successfully added players' names, separated with a comma and a space (", ") in the format:
            "Successfully added: {name1}, {name2}, … {nameN}"


        """
        for player in args:
            if player in self.players:
                continue
            self.players.append(player)
            self.player_by_player_names[player.name] = player
        return f"Successfully added: {', '.join(self.player_by_player_names.keys())}"

    def add_supply(self, *args):
        """
        Add all supplies to the 'supplies'
•	    A supply could be added multiple times


        """
        for suply in args:
            self.supplies.append(suply)

    def sustain(self, player_name: str, sustenance_type: str, ):
        """
        Use the last supply added from the given type to sustain the player:
            -increase his stamina with the supply's energy value
            -remove the supply from 'supplies'
            -return the message "{player_name} sustained successfully with {supply_name}."
        A player always uses the whole amount (units) of the given supply, but his stamina cannot enhance above 100 (it should be set to 100).

        If the player doesn't need sustenance:
            -return the message "{player_name} have enough stamina."
        If the given type is food, but there is no food left:
            -raise an Exception with the message "There are no food supplies left!"
        If the given type is drink, but there are no drinks left:
            -raise an Exception with the message "There are no drink supplies left!"
•	    The valid sustenance types are "Food" and "Drink":
            -In any other case, ignore the command.
•	    If the player is not in the 'players':
            -ignore the command.


        """
        player = self.__search_player_by_name(player_name)
        corect_type = 'Food', 'Drink'
        if player not in self.players or sustenance_type not in corect_type:
            return
        self.__validate_player_doesnt_need_susteance(player)
        if sustenance_type == 'Food':
            self.__validate_no_food(sustenance_type)
        elif sustenance_type == 'Drink':
            self.__validate_no_drink(sustenance_type)
        self.__take_suplly(sustenance_type, player)

        return f"{player_name} sustained successfully with {supply}."

    def duel(self,first_player_name: str, second_player_name: str):
        """
        The two players participate in a duel, each of them could only attack once.
            If a 'player.stamina' is 0 -he could not participate in a duel.
                -return a message "Player {player_name} does not have enough stamina."
                -discontinue the duel.
             If both players' stamina is 0:
                -return the message for both players on separate lines, starting from the first one given.
        If both players have a positive value of stamina, the duel begins:
        The player with a lower value of stamina attacks first.
            -He reduces the other player's stamina by a value equal to one-half of his own (the attacker's) stamina.
        Next, the other player attacks the same way:
            -reduces the first player's stamina by a value equal to one-half of his own (the second attacker's) stamina).
        If, during the duel, a player's stamina becomes equal to or less than 0, it should be set to 0.
            -The player immediately loses the duel
            -the other player becomes a winner.
        Otherwise, the winner is the player who has left with more stamina.
        Return the winner's name in the format: "Winner: {winner_name}"
        Note: there will be no case where both players will have equal stamina values at the beginning or in the end.
        Note: the players will always exist in the players list.

        """

        first_player = self.__search_player_by_name(first_player_name)
        second_player = self.__search_player_by_name(second_player_name)

        self.__validate_zerro_stanima(first_player, second_player)

        self.__duel(first_player, second_player)
        self.__check_stamina_is_positive(first_player, second_player)
        self.__duel(first_player, second_player)
        self.__winner(first_player, second_player)

    def next_day(self):
        """
        First, the 'stamina' of each added player gets reduced by the result of multiplying their age by 2
            If a 'player.stamina' becomes less than 0:
                -it should be set to 0
•	    Then, you need to sustain each player by giving them:
            one food (first) and one drink (second)

        """

        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            player.stamina = min(player.stamina + drink.energy, 100)
            player.stamina = min(player.stamina + Food.energy, 100)

    def __str__(self):
        result =''
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}/n"
        for supply in self.supplies:
            result += f'{supply.type}: {supply.name}, {supply.energy}/n'
        return result.strip()



    def __search_player_by_name(self, player_name) -> Player:
        return self.player_by_player_names.get(player_name, None)

    def __take_suplly(self, sustenance_type, player):
        for i in range(len(self.supplies) - 1, -1, -1):
            teaked_supply = self.supplies.pop(i)
            name = teaked_supply.__class__.__name__
            if name == sustenance_type:
                player.stamina = min(player.stamina + teaked_supply.energy, player.MAX_STAMINA)
                return player.stamina
            else:
                self.supplies.append(teaked_supply)

    def __validate_player_doesnt_need_susteance(self, player):
        if player.stamina == player.MAX_STAMINA:
            return f"{player.name} have enough stamina."

    def __validate_no_food(self, sustenance_type):
            for i in range(len(self.supplies) - 1, -1, -1):
                teaked_supply = self.supplies[i]
                name = teaked_supply.__class__.__name__
                if name == sustenance_type:

                    continue
            else:
                raise Exception(self.NO_FOOD_ERROR_MESSAGE)


    def __validate_no_drink(self, sustenance_type):
        for i in range(len(self.supplies) - 1, -1, -1):
            teaked_supply = self.supplies[i]
            name = teaked_supply.__class__.__name__
            if name == sustenance_type:
                break
        else:
            raise Exception(self.NO_DRINK_ERROR_MESSAGE)

    def __duel(self, first_player, second_player):
        if first_player.stamina < second_player.stamina:
           return max(second_player.stamina - first_player.stamina * 0.5, 0)
        return max(first_player.stamina - second_player.stamina *0.5, 0)

    def __check_stamina_is_positive(self, first_player, second_player):
        if first_player.stamina == 0:
            return f"Winner: {second_player.name}"
        elif second_player.stamina == 0:
            return f"Winner: {first_player.name}"
        return True

    def __winner(self, first_player, second_player):
        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        return f"Winner: {second_player.name}"

    def __validate_zerro_stanima(self,first_player, second_player):
        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."
        elif first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."\
                    f"Player {second_player.name} does not have enough stamina."
    
    
    
        
