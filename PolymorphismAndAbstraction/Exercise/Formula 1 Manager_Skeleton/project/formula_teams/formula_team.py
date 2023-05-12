from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET = 1000000

    def __init__(self, budget: int):
        self.budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__validate_budget(value)
        self.__budget = value

    def __validate_budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
