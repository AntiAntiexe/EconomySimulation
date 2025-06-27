import matplotlib.pyplot as plt
import pandas as pd

firmData = pd.read_csv('firms.csv')


figure, axis = plt.subplots(2, 2)

axis[0, 0].plot(firmData['Day'], firmData['Money'], label='Money')
axis[0, 0].set_title("Firm Money Over Time")

axis[0, 1].plot(firmData['Day'], firmData['Goods'], label='Goods')
axis[0, 1].set_title("Firm Goods Over Time")

axis[1, 0].plot(firmData['Day'], firmData['GoodsPrice'], label='Goods Price')
axis[1, 0].set_title("Firm Goods Price Over Time")

axis[1, 1].plot(firmData['Day'], firmData['Land'], label='Land')
axis[1, 1].plot(firmData['Day'], firmData['Labour'], label='Labour')
axis[1, 1].plot(firmData['Day'], firmData['Capital'], label='Capital')
axis[1, 1].set_title("Firm Land Over Time")

axis[1, 1].legend()

plt.show()


