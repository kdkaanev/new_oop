import re


class Customer:
    id = 1
    def __init__(self, name, address, email, id = 1):
        self.name = name
        self.address = address
        self.email = email
        
    

    @classmethod
    def get_next_id(cls, name, address, email):
        Customer.id += 1
        return cls(name, address, email, id)

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

