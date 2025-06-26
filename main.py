

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
        self.goodsP = 0.0
    
    def goodsPrice(self, landPrice: float, labourPrice: float, capitalPrice: float, goodsBias: float):
        self.goodsP = self.land_price + self.labour_price + self.capital_price) + goodsBias

     


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
                        Lprice = firm.wage + household.bias 
                        firm.land += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.land -= 1
                        firm.money -= (firm.wage - firm.bias)
                        Lprice = firm.wage - firm.bias
                        firm.land += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.land -= 1
                        firm.money -= firm.wage
                        Lprice = firm.wage
                        firm.land += 1
                    

                if household.labour > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage + household.bias)
                        LanPrice = firm.wage + household.bias
                        firm.labour += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage - firm.bias)
                        LanPrice = firm.wage - firm.bias
                        firm.labour += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.labour -= 1
                        firm.money -= firm.wage
                        LanPrice = firm.wage
                        firm.labour += 1

                if household.capital > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage + household.bias)
                        CPrice = firm.wage + household.bias
                        firm.capital += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage - firm.bias)
                        CPrice = firm.wage - firm.bias
                        firm.capital += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.capital -= 1
                        firm.money -= firm.wage
                        CPrice = firm.wage
                        firm.capital += 1

                firm.goodsPrice(Lprice, LanPrice, CPrice)
     
        
        for firm in self.firms:
            if firm.land > 0 and firm.labour > 0 and firm.capital > 0:
                firm.goods += 1
                firm.land -= 1
                firm.labour -= 1
                firm.capital -= 1

        for firm in self.firms:
            for household in self.households:
                if firm.goods > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        firm.money += (firm.goodsP - household.bias)
                        household.income -= (firm.goodsP - household.bias)
                        household.goods += 1
                        firm.goods -= 1
                    elif household.negotiation_value < firm.negotiation_value:
                        firm.money += (firm.goodsP + firm.bias)
                        household.income -= (firm.goodsP + firm.bias)
                        household.goods += 1
                        firm.goods -= 1
                    elif household.negotiation_value == firm.negotiation_value:
                        firm.money += firm.goodsP
                        household.income -= firm.goodsP
                        household.goods += 1
                        firm.goods -= 1
                
