import streamlit as st
import numpy as np
import pandas as pd
from game.runFiles.graph2 import Graph 




householdData = pd.read_csv('data/households.csv')

firmData = pd.read_csv('data/firms.csv')

governmentData = pd.read_csv('data/government.csv')

st.title("Economy Simulation Data Visualization")
st.subheader("Household Data")
graph = Graph()
graph.graphHouseholds(householdData, legend=False)
graph.graphFirms(firmData, legend=False)
graph.graphGovernment(governmentData, legend=False)
st.pyplot(graph.HouseHoldfigure)
st.pyplot(graph.Frimfigure)
st.pyplot(graph.Governmentfigure)