class Equipment:
    id = 1
    def __init__(self, name, id = 1):
        self.name = name
        self.id = id

    @classmethod
    def get_next_id(cls, name):
        Equipment.id += 1
        return cls(name, id)

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"