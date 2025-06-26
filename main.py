

class HouseHold:
    def __init__(self, Land: int, Labour: int, Capital: int):
        self.land = Land
        self.labour = Labour
        self.capital = Capital
        self.income = 0
        self.goods = 0
    
class Firm:
    def __init__(self, Money: float, Wage: float):
        self.money = Money
        self.wage = Wage
        self.goods = 0
        self.labor = 0
        self.capital = 0
        self.land = 0


class Simulation:
    def __init__(self, Households: list, Firms: list):
        self.households = Households
        self.firms = Firms
        self.time = 0
    
    def step(self)