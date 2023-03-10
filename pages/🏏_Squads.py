import streamlit as st
import pandas as pd

df = pd.read_csv("Squads/Week1.csv")
st.header("Week 1 squad")
st.dataframe(df)

df = pd.read_csv("Squads/Week2.csv")
st.header("Week 2 squad")
st.dataframe(df)
