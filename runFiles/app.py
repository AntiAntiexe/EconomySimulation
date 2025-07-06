import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




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

st.pyplot(figure)

firmData = pd.read_csv('data/firms.csv')


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
axis[1, 1].set_title("Firm Resources Over Time")

axis[1, 1].legend()

st.pyplot(figure)