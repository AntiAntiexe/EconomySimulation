import random


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
    def __init__(self, Money: float, Wage: float, NegotiationVal: float, Bias: float, goodsBias: float):
        self.goodsBias = goodsBias
        self.bias = Bias
        self.negotiation_value = NegotiationVal
        self.money = Money
        self.wage = Wage
        self.goods = 0
        self.labour = 0
        self.capital = 0
        self.land = 0
        self.goodsP = 0.0

        self.land_price = 0.0
        self.labour_price = 0.0
        self.capital_price = 0.0
    
    def goodsPrice(self, landPrice: float, labourPrice: float, capitalPrice: float):
        self.goodsP = landPrice + labourPrice + capitalPrice + self.goodsBias

     


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
                        firm.land_price = firm.wage + household.bias
                        firm.land += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.land -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.land_price = firm.wage - firm.bias
                        firm.land += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.land -= 1
                        firm.money -= firm.wage
                        firm.land_price = firm.wage
                        firm.land += 1
                    
                if household.labour > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage + household.bias)
                        firm.labour_price = firm.wage + household.bias
                        firm.labour += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.labour -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.labour_price = firm.wage - firm.bias
                        firm.labour += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.labour -= 1
                        firm.money -= firm.wage
                        firm.labour_price = firm.wage
                        firm.labour += 1

                if household.capital > 0:
                    if household.negotiation_value > firm.negotiation_value:
                        household.income += (firm.wage + household.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage + household.bias)
                        firm.capital_price = firm.wage + household.bias
                        firm.capital += 1
                    elif household.negotiation_value < firm.negotiation_value:
                        household.income += (firm.wage - firm.bias)
                        household.capital -= 1
                        firm.money -= (firm.wage - firm.bias)
                        firm.capital_price = firm.wage - firm.bias
                        firm.capital += 1
                    elif household.negotiation_value == firm.negotiation_value:
                        household.income += firm.wage
                        household.capital -= 1
                        firm.money -= firm.wage
                        firm.capital_price = firm.wage
                        firm.capital += 1

                firm.goodsPrice(firm.land_price, firm.labour_price, firm.capital_price)

        
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
                
class App:
    def __init__(self, numberOfFirms: int, numberOfHouseholds: int, days: int):
        self.households = []
        self.firms = []
        self.numberOfFirms = numberOfFirms
        self.numberOfHouseholds = numberOfHouseholds

    def createHouseholds(self):
        for i in range(self.numberOfHouseholds):
            land = random.randint(10, 100)
            landPrice = random.uniform(1.0, 10.0)
            labour = random.randint(10, 100)
            labourPrice = random.uniform(1.0, 10.0)
            capital = random.randint(10, 100)
            capitalPrice = random.uniform(1.0, 10.0)
            negotiationVal = random.uniform(1.0, 10.0)
            bias = random.uniform(1.0, 5.0)
            self.households.append(HouseHold(land, landPrice, labour, labourPrice, capital, capitalPrice, negotiationVal, bias))

    def createFirms(self):
        for i in range(self.numberOfFirms):
            money = random.uniform(100.0, 1000.0)
            wage = random.uniform(1.0, 10.0)
            negotiationVal = random.uniform(1.0, 10.0)
            bias = random.uniform(1.0, 5.0)
            goodsBias = random.uniform(1.0, 2.0)
            self.firms.append(Firm(money, wage, negotiationVal, bias, goodsBias))



mainApp = App(10, 10, 360)
mainApp.createHouseholds()
mainApp.createFirms()

simulation = Simulation(mainApp.households, mainApp.firms)
for day in range(360):
    simulation.step()
    print(f'Day {day +1}:')
    for i, household in enumerate(simulation.households):
        print(f'Household {i + 1}: Income: {household.income}, Goods: {household.goods}, Land: {household.land}, Labour: {household.labour}, Capital: {household.capital}')
    for i, firm in enumerate(simulation.firms):
        print(f'Firm {i + 1}: Money: {firm.money}, Goods: {firm.goods}, Land: {firm.land}, Labour: {firm.labour}, Capital: {firm.capital}, Goods Price: {firm.goodsP}')
    print('---')