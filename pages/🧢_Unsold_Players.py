import streamlit as st
import pandas as pd

df = pd.read_csv("Unsold_players.csv")
st.header("Unsold Players")
# st.dataframe(df)
st.table(df)
