class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transaction = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.transaction.append(amount)
        self.amount += amount

    @property
    def balance(self):
        return sum(self.transaction) + self.amount

    def validate_transaction(self, account, amount_to_add):
        if amount_to_add < 0 or self.balance <= 0:
            raise ValueError("sorry cannot go in debt!")
        self.add_transaction(amount_to_add)
        return f"New balance: {self.balance}"

    def __repr__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __str__(self):
        return f"Account({self.owner}, {self.balance})"

    def __len__(self):
        return len(self.transaction)

    def __getitem__(self, item):
        self.transaction.reverse()
        return self.transaction[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc_name = f'{self.owner} {other.owner}'
        new_amount = self.amount + other.amount
        return Account(acc_name, new_amount)







acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

