# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
from st_aggrid import AgGrid

st.title('PIKP Formula 1')

st.write('Prikaz dataframea voznikov')
df_drivers = pd.read_csv('data/drivers.csv') # ja
AgGrid(df_drivers)

df_circuits = pd.read_csv('data/circuits.csv')
df_constructorResults = pd.read_csv('data/constructorResults.csv')
df_constructors = pd.read_csv('data/constructors.csv')
dc_constructorStandings = pd.read_csv('data/constructorStandings.csv')
df_driverStandings = pd.read_csv('data/driverStandings.csv') # ja
df_lapTimes = pd.read_csv('data/lapTimes.csv') # ja
df_pitStops = pd.read_csv('data/pitStops.csv') # ja
df_qualifying = pd.read_csv('data/qualifying.csv')
df_races = pd.read_csv('data/races.csv')
df_seasons = pd.read_csv('data/seasons.csv')
df_sprintResults = pd.read_csv('data/sprintResults.csv')
df_status = pd.read_csv('data/status.csv')

df_merged = df_drivers.merge(df_driverStandings, how='inner', on='driverId')
df_merged = df_merged.merge(df_lapTimes, how='inner', on='driverId')
df_merged = df_merged.merge(df_pitStops, how='inner', on='driverId')

@st.cache
def load_data():
  voznik_nacionalnost_povprecen_cas = df_merged.groupby(['driverId', 'nationality']).mean()
  return voznik_nacionalnost_povprecen_cas

voznik_nacionalnost_povprecen_cas = load_data()
print(voznik_nacionalnost_povprecen_cas.head(10))

df_dva = df_merged.groupby(['driverRef']).mean()
plot = plt.plot(df_dva['points'])
plot = plt.ylabel('Povprecne tocke na tekmo')
plot = plt.xticks(np.arange(0, len(df_dva), 1.0), df_dva.index, rotation=90)
st.pyplot(plt)


st.write('Rok Kukovec, Domen Leš')