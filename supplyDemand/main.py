import matplotlib.pyplot as plt
import pandas as pd
import csv

class SupplyDemand:
    def __init__(self):
        self.price = 10

    def update(self):
        Qd = 100 - 2*self.price
        Qs = 20 + 3*self.price
        
        if Qd > Qs:
            self.price += 0.1
        elif Qd < Qs:
            self.price -= 0.1
        
        
        return self.price, Qd, Qs
    
supply_demand = SupplyDemand()

def saveData(day, price, Qd, Qs):
        data = {'Day': day, 'Price': price, 'QuantityDemanded': Qd, 'QuantitySupplied': Qs}
        
        with open('supplyDemand\supply_demand.csv', 'a', newline='') as csvfile:
            fieldnames = ['Day', 'Price', 'QuantityDemanded', 'QuantitySupplied']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(data)
def writeHeaders():
    with open('supplyDemand\supply_demand.csv', 'w', newline='') as csvfile:
        fieldnames = ['Day', 'Price', 'QuantityDemanded', 'QuantitySupplied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

writeHeaders()

for day in range(1000):
    price, Qd, Qs = supply_demand.update()
    saveData(day, price, round(Qd, 2), round(Qs, 2))
    print(f"Day {day}: Price: {price:.2f}, Quantity Demanded: {Qd:.2f}, Quantity Supplied: {Qs:.2f}")
    if round(Qd, 2) == round(Qs, 2):
        print(f"Equilibrium reached on Day {day}: Price: {price:.2f}, Quantity Demanded: {Qd:.2f}, Quantity Supplied: {Qs:.2f}")
        break
    
    
