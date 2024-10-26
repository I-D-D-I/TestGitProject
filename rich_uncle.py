class rich_uncle:
    def __init__(self, balance, name, cash = 500):
        self.balance = balance
        self.country = 'Italy'
        self.name = name
        self.__cash = cash

    def get_private_plane(self):
        print(f'Sir {self.name}, your plane is here')

    def get_cash(self):
        print(f'I have {self.__cash} dollars')

    def set_cash(self, cash):
        self.__cash = cash

class plemyannik(rich_uncle):
    def get_private_plane(self):
        print(f'Sir {self.name}, plane is not yours')

andrey = plemyannik(100, "Andrey")
andrey.get_private_plane()

uncle_john = rich_uncle(4000000, 'John')
# uncle_john.balance = 1000

uncle_sam = rich_uncle(5000000, 'Sam', cash = 300)

print(uncle_sam.balance)
print(uncle_sam.name)
print(uncle_john.balance)
uncle_john.get_private_plane()
uncle_sam.set_cash(150)
uncle_sam.get_cash()