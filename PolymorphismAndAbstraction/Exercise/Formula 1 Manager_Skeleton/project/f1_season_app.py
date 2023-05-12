from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAM_NAME = [
        "Red Bull",
        "Mercedes"
    ]
    NAME_ERROR_MESSAGE = "Invalid team name!"
    NOT_REGISTRD_TEAM_ERROR_MESSAGE = "Not all teams have registered for the season."

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        self.__check_valid_tem_name(team_name)
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        self.__check_team_registred()
        winer = self.__check_position(red_bull_pos, mercedes_pos)
        red_bull_message = RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)
        mercedes_message = MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)
        return f"Red Bull: {red_bull_message}. Mercedes: {mercedes_message}. {winer} is ahead at the {race_name} race."

    def __check_valid_tem_name(self, name):
        if name not in self.VALID_TEAM_NAME:
            raise ValueError(self.NAME_ERROR_MESSAGE)

    def __check_team_registred(self):
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception(self.NOT_REGISTRD_TEAM_ERROR_MESSAGE)

    def __check_position(self, red_bull_pos, mercedes_pos):
        if red_bull_pos < mercedes_pos:
            return 'Red Bull'
        else:
            return 'Mercedes'
