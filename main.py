

class HouseHold:
    def __init__(self, Land: int, LandPrice: float, Labour: int, LabourPrice: float, Capital: int, CapitalPrice: float, NegotiationVal: float, Bias: float):
        self.land_price = LandPrice
        self.labour_price = LabourPrice
        self.capital_price = CapitalPrice
        self.negotiation_value = NegotiationVal
        self.bias = Bias
        self.land = Land
        self.labour = Labour
        self.capital = Capital
        self.income = 0
        self.goods = 0
    
class Firm:
    def __init__(self, Money: float, Wage: float, NegotiationVal: float, Bias: float):
        self.bias = Bias
        self.negotiation_value = NegotiationVal
        self.money = Money
        self.wage = Wage
        self.goods = 0
        self.labour = 0
        self.capital = 0
        self.land = 0

     


class Simulation:
    def __init__(self, Households: list, Firms: list):
        self.households = Households
        self.firms = Firms
        self.time = 0

    def step(self):
        self.time += 1

        for household in self.households:
            for firm in self.firms:
                if household.land > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.land -= 1
                        firm.money -= (firm.wage + household.bias)
                        firm.land += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.land -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.land += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.land -= 1
                        firm.money -= firm.wage
                        firm.land += 1

                if household.labour > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage + household.bias)
                        firm.labour += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.labour += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.labour -= 1
                        firm.money -= firm.wage
                        firm.labour += 1

                if household.capital > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage + household.bias)
                        firm.capital += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.capital += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.capital -= 1
                        firm.money -= firm.wage
                        firm.capital += 1
        
        for firm in self.firms:
            
                

        
