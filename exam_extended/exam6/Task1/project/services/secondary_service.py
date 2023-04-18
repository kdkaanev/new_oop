from project.services.base_service import BaseService


class SecondaryService(BaseService):
    BASE_CAPACITY = 15

    def __init__(self, name: str, capacity: int = None):
        self.capacity = capacity if capacity else self.BASE_CAPACITY
        super().__init__(name, capacity)


    def details(self):
        if len(self.robots) == 0:
            return f"{self.name} Main Service:'\n'" \
                   f"Robots: none"
        else:
            return f"{self.name} Main Service:'\n'" \
                   f'Robots : {" ".join(n for n in self.robots)}'

