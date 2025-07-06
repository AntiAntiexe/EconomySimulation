import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from graph2 import Graph 




householdData = pd.read_csv('data/households.csv')

firmData = pd.read_csv('data/firms.csv')

st.title("Economy Simulation Data Visualization")
st.subheader("Household Data")
graph = Graph()
graph.graphHouseholds(householdData, legend=False)
graph.graphFirms(firmData, legend=False)
st.pyplot(graph.HouseHoldfigure)
st.pyplot(graph.Frimfigure)