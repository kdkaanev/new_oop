from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250000
    SPONSORS_INCOMING = {
        1: 1500000,
        2: 800000,
        8: 20000,
        10: 10000
    }

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0
        for pos, money in self.SPONSORS_INCOMING.items():
            if pos == race_pos:
                earned_money += money
        revenue = earned_money - self.EXPENSES_PER_RACE
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
