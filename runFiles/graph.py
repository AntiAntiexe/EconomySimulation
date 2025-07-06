import matplotlib.pyplot as plt
import pandas as pd

firmData = pd.read_csv('data/firms.csv')


figure, axis = plt.subplots(2, 3)
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

plt.show()


'''

axis[0, 0].plot(firmData['Day'], firmData['Money'], label='Money')
axis[0, 0].set_title("Firm Money Over Time")

axis[0, 1].plot(firmData['Day'], firmData['Goods'], label='Goods')
axis[0, 1].set_title("Firm Goods Over Time")

axis[1, 0].plot(firmData['Day'], firmData['GoodsPrice'], label='Goods Price')
axis[1, 0].set_title("Firm Goods Price Over Time")

axis[1, 1].plot(firmData['Day'], firmData['Land'], label='Land')
axis[1, 1].plot(firmData['Day'], firmData['Labour'], label='Labour')
axis[1, 1].plot(firmData['Day'], firmData['Capital'], label='Capital')
axis[1, 1].set_title("Firm Resources Over Time")

axis[1, 1].legend()

plt.show()


