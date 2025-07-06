import pandas as pd
import matplotlib.pyplot as plt

householdData = pd.read_csv('data/households.csv')

figure, axis = plt.subplots(3)

figure.tight_layout(pad=3.0)

axis[0].plot(householdData['Day'], householdData['Income'], label='Income')
axis[0].set_title("Household Money Over Time")

axis[1].plot(householdData['Day'], householdData['Goods'], label='Goods')
axis[1].set_title("Household Goods Over Time")

axis[2].plot(householdData['Day'], householdData['Land'], label='Land')
axis[2].plot(householdData['Day'], householdData['Labour'], label='Labour')
axis[2].plot(householdData['Day'], householdData['Capital'], label='Capital')
axis[2].set_title("Household Resources Over Time")

axis[2].legend()

plt.show()