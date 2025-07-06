import pandas as pd
import matplotlib.pyplot as plt
'''
householdData = pd.read_csv('data/households.csv')

figure, axis = plt.subplots(2, 3)

figure.tight_layout(pad=3.0)

datasets = []

for i in householdData['DataSet'].unique():
    datasets.append(householdData.loc[householdData['DataSet'] == i])

for data in datasets:
    axis[0, 0].plot(data['Day'], data['Income'], label=data['DataSet'].iloc[0])
    axis[0, 1].plot(data['Day'], data['Goods'], label=data['DataSet'].iloc[0])
    axis[0, 2].plot(data['Day'], data['Land'], label=data['DataSet'].iloc[0])
    axis[1, 0].plot(data['Day'], data['Labour'], label='Labour')
    axis[1, 1].plot(data['Day'], data['Capital'], label=data['DataSet'].iloc[0])


axis[0, 0].set_title("Household Money Over Time")
axis[0, 1].set_title("Household Goods Over Time")
axis[0, 2].set_title("Household Land Over Time")
axis[1, 0].set_title("Household Labour Over Time")
axis[1, 1].set_title("Household Capital Over Time")  





plt.show()
'''


class Graph:
    def graphHouseholds(self, householdData: pd.DataFrame, legend: bool):
        self.HouseHoldfigure, axis = plt.subplots(2, 3)

        datasets = []

        for i in householdData['DataSet'].unique():
            datasets.append(householdData.loc[householdData['DataSet'] == i])

        for data in datasets:
            axis[0, 0].plot(data['Day'], data['Income'], label=data['DataSet'].iloc[0])
            axis[0, 1].plot(data['Day'], data['Goods'], label=data['DataSet'].iloc[0])
            axis[0, 2].plot(data['Day'], data['Land'], label=data['DataSet'].iloc[0])
            axis[1, 0].plot(data['Day'], data['Labour'], label='Labour')
            axis[1, 1].plot(data['Day'], data['Capital'], label=data['DataSet'].iloc[0])


        axis[0, 0].set_title("Household Money Over Time")
        axis[0, 1].set_title("Household Goods Over Time")
        axis[0, 2].set_title("Household Land Over Time")
        axis[1, 0].set_title("Household Labour Over Time")
        axis[1, 1].set_title("Household Capital Over Time")  

        if legend:
            axis[0, 0].legend()
            axis[0, 1].legend()
            axis[0, 2].legend()
            axis[1, 0].legend()
            axis[1, 1].legend()

    def graphFirms(self, firmData: pd.DataFrame, legend: bool):
        
        self.Frimfigure, axis = plt.subplots(2, 3)
        plt.tight_layout(pad=3.0)

        datasets = []

        for i in firmData['DataSet'].unique():
            datasets.append(firmData.loc[firmData['DataSet'] == i])

        for data in datasets:
            axis[0, 0].plot(data['Day'], data['Money'], label=data['DataSet'].iloc[0])
            axis[0, 1].plot(data['Day'], data['Goods'], label=data['DataSet'].iloc[0])
            axis[0, 2].plot(data['Day'], data['GoodsPrice'], label=data['DataSet'].iloc[0])
            axis[1, 0].plot(data['Day'], data['Land'], label=data['DataSet'].iloc[0])
            axis[1, 1].plot(data['Day'], data['Labour'], label=data['DataSet'].iloc[0])
            axis[1, 2].plot(data['Day'], data['Capital'], label=data['DataSet'].iloc[0])


        axis[0, 0].set_title("Firm Money Over Time")
        axis[0, 1].set_title("Firm Goods Over Time")
        axis[0, 2].set_title("Firm Goods Price Over Time")
        axis[1, 0].set_title("Firm Land Over Time")
        axis[1, 1].set_title("Firm Labour Over Time")
        axis[1, 2].set_title("Firm Capital Over Time")

        if legend:
            axis[0, 0].legend()
            axis[0, 1].legend()
            axis[0, 2].legend()
            axis[1, 0].legend()
            axis[1, 1].legend()
            axis[1, 2].legend()



