import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('supplyDemand/supply_demand.csv')

#plt.plot(data['Day'], data['Price'], label='Price')
plt.plot(data['QuantityDemanded'], data['Price'], label='Quantity Demanded')
plt.plot(data['QuantitySupplied'], data['Price'], label='Quantity Supplied')




plt.show()
