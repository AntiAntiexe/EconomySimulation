import random
import csv
import sys
old_stdout = sys.stdout

log_file = open("output.log","w")

sys.stdout = log_file


class HouseHold:
    def __init__(self, name: str, Land: int, LandPrice: float, Labour: int, LabourPrice: float, Capital: int, CapitalPrice: float, NegotiationVal: float, Bias: float):
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
        self.name = name
    
class Firm:
    def __init__(self, name: str, Money: float, Wage: float, NegotiationVal: float, Bias: float, goodsBias: float):
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

        self.name = name
    
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
            while firm.land >0 and firm.labour > 0 and firm.capital > 0:
                print('producing')
                firm.goods += 1
                firm.land -= 1
                firm.labour -= 1
                firm.capital -= 1

        print(f'Day {day +1}:')
        for i, household in enumerate(self.households):
            print(f'Household {i + 1}: Income: {household.income}, Goods: {household.goods}, Land: {household.land}, Labour: {household.labour}, Capital: {household.capital}')
        for i, firm in enumerate(self.firms):
            print(f'Firm {i + 1}: Money: {firm.money}, Goods: {firm.goods}, Land: {firm.land}, Labour: {firm.labour}, Capital: {firm.capital}, Goods Price: {firm.goodsP}')

        for firm in self.firms:
            for household in self.households:
                if firm.goods > 0 and household.income >= firm.goodsP:
                    if household.negotiation_value > firm.negotiation_value:
                        firm.money += (firm.goodsP - household.bias)
                        household.income -= (firm.goodsP - household.bias)
                        household.goods += 1
                        firm.goods -= 1
                        print('sold')
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
            land = random.randint(1000, 10000)
            landPrice = random.uniform(1.0, 10.0)
            labour = random.randint(1000, 10000)
            labourPrice = random.uniform(1.0, 10.0)
            capital = random.randint(1000, 10000)
            capitalPrice = random.uniform(1.0, 10.0)
            negotiationVal = random.uniform(1.0, 10.0)
            bias = random.uniform(1.0, 5.0)
            name = f'Household{i + 1}'
            self.households.append(HouseHold(name, land, landPrice, labour, labourPrice, capital, capitalPrice, negotiationVal, bias))

    def createFirms(self):
        for i in range(self.numberOfFirms):
            money = random.uniform(100.0, 1000.0)
            wage = random.uniform(1.0, 10.0)
            negotiationVal = random.uniform(1.0, 10.0)
            bias = random.uniform(1.0, 5.0)
            goodsBias = random.uniform(1.0, 10.0)
            name = f'Firm{i + 1}'
            self.firms.append(Firm(name, money, wage, negotiationVal, bias, goodsBias))

    def saveHouseholds(self, dataSet, day, income, goods, land, labour, capital):
        data = {'DataSet': dataSet, 'Day': day, 'Income': income, 'Goods': goods, 'Land': land, 'Labour': labour, 'Capital': capital}

        with open('data/households.csv', 'a', newline='') as csvfile:
            fieldnames = ['DataSet', 'Day', 'Income', 'Goods', 'Land', 'Labour', 'Capital']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(data)

    def saveFirms(self, dataSet, day, money, goods, goodsPrice, land, labour, capital):
        data = {'DataSet': dataSet,'Day': day, 'Money': money, 'Goods': goods, 'GoodsPrice': goodsPrice, 'Land': land, 'Labour': labour, 'Capital': capital}

        with open('data/firms.csv', 'a', newline='') as csvfile:
            fieldnames = ['DataSet', 'Day', 'Money', 'Goods', 'GoodsPrice', 'Land', 'Labour', 'Capital']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(data)
    
    def writeHeaders(self):
        with open('data/households.csv', 'w', newline='') as csvfile:
            fieldnames = ['DataSet', 'Day', 'Income', 'Goods', 'Land', 'Labour', 'Capital']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        with open('data/firms.csv', 'w', newline='') as csvfile:
            fieldnames = ['DataSet', 'Day', 'Money', 'Goods', 'GoodsPrice', 'Land', 'Labour', 'Capital']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()



mainApp = App(10, 10, 360)
mainApp.createHouseholds()
mainApp.createFirms()

simulation = Simulation(mainApp.households, mainApp.firms)

mainApp.writeHeaders()

for day in range(360):
    simulation.step()

    for i, household in enumerate(simulation.households):
        mainApp.saveHouseholds(simulation.households[i].name, day + 1, simulation.households[i].income, simulation.households[i].goods, simulation.households[i].land, simulation.households[i].labour, simulation.households[i].capital)
    for i, firm in enumerate(simulation.firms):
        mainApp.saveFirms(simulation.firms[i].name, day + 1, simulation.firms[i].money, simulation.firms[i].goods, simulation.firms[i].goodsP, simulation.firms[i].land, simulation.firms[i].labour, simulation.firms[i].capital)
    
    print('---')

sys.stdout = old_stdout
log_file.close()