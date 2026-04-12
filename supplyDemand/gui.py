import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox
from tkinter import font


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Supply and Demand Simulation")
        self.root.geometry("800x600")

        self.label = ttk.Label(self.root, text="Supply and Demand Simulation", font=("Arial", 20, "bold"))
        self.label.place(x=20, y=20, anchor='nw')
        
        self.demandLabel = ttk.Label(self.root, text="Demand", font=("Arial", 16, "bold"))
        self.demandLabel.place(x=20, y=60, anchor='nw')
        
        self.D1_priceQuantityLabel = ttk.Label(self.root, text="Price and Quantity (e.g.: 10, 100):", font=("Arial", 14))
        self.D1_priceQuantityLabel.place(x=20, y=90, anchor='nw')
        self.D1_priceQuantityEntry = ttk.Entry(self.root)
        self.D1_priceQuantityEntry.place(x=325, y=92.5, anchor='nw')
        
        self.D2_priceQuantityLabel = ttk.Label(self.root, text="Price and Quantity (e.g.: 10, 100):", font=("Arial", 14))
        self.D2_priceQuantityLabel.place(x=20, y=130, anchor='nw')
        self.D2_priceQuantityEntry = ttk.Entry(self.root)
        self.D2_priceQuantityEntry.place(x=325, y=132.5, anchor='nw')
        
        self.supplyLabel = ttk.Label(self.root, text="Supply", font=("Arial", 16, "bold"))
        self.supplyLabel.place(x=20, y=160, anchor='nw')
        
        self.S1_priceQuantityLabel = ttk.Label(self.root, text="Price and Quantity (e.g.: 10, 100):", font=("Arial", 14))
        self.S1_priceQuantityLabel.place(x=20, y=190, anchor='nw')
        self.S1_priceQuantityEntry = ttk.Entry(self.root)
        self.S1_priceQuantityEntry.place(x=325, y=192.5, anchor='nw')
        
        self.S2_priceQuantityLabel = ttk.Label(self.root, text="Price and Quantity (e.g.: 10, 100):", font=("Arial", 14))
        self.S2_priceQuantityLabel.place(x=20, y=230, anchor='nw')
        self.S2_priceQuantityEntry = ttk.Entry(self.root) 
        self.S2_priceQuantityEntry.place(x=325, y=232.5, anchor='nw')
        
        self.CurrentPriceLabel = ttk.Label(self.root, text="Current Price: ", font=("Arial", 16))
        self.CurrentPriceLabel.place(x=20, y=270, anchor='nw')
        self.CurrentPriceEntry = ttk.Entry(self.root)
        self.CurrentPriceEntry.place(x=160, y=272.5, anchor='nw')
        
        self.simulateButton = ttk.Button(self.root, text="Simulate", command=self.simulation)
        self.simulateButton.place(x=400, y=500, anchor='center')


    def simulation(self):
        pass

class SupplyDemandSimulation:
    def __init__(self, Dpq1 : list, Dpq2: list, Spq1: list, Spq2: list, currentPrice: float):
        
        Dq1 = Dpq1[1] 
        Dp1 = Dpq1[0]
        
        Dq2 = Dpq2[1]
        Dp2 = Dpq2[0]
        
        Sq1 = Spq1[1]
        Sp1 = Spq1[0]
        
        Sq2 = Spq2[1]
        Sp2 = Spq2[0]

        self.currentPrice = currentPrice
        
        
    def getSupplyDemandEquations(self):
        self.Qd = (self.Dq2 - self.Dq1) / (self.Dp2 - self.Dp1) * (self.currentPrice - self.Dp1) + self.Dq1
        self.Qs = (self.Sq2 - self.Sq1) / (self.Sp2 - self.Sp1) * (self.currentPrice - self.Sp1) + self.Sq1
         

    def updatePrice(self):
        if self.Qd > self.Qs:
            self.currentPrice += 0.1
        elif self.Qd < self.Qs:
            self.currentPrice -= 0.1
        
        return self.currentPrice, self.Qd, self.Qs
        


app = tk.Tk()
app_instance = App(app)
app.mainloop()