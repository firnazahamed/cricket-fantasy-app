import streamlit as st
import pandas as pd

score_df = pd.read_csv("./Outputs/score_df.csv", index_col="Owner")
st.header("Match wise player points")
st.dataframe(score_df)

sum_df = pd.read_csv("./Outputs/sum_df.csv", index_col="Owner")
st.header("Match aggregate points")
st.dataframe(sum_df)

cumsum_df = pd.read_csv("./Outputs/cumsum_df.csv", index_col="Owner")
st.header("Cumulative points")
st.dataframe(cumsum_df)

weekly_points_df = pd.read_csv("./Outputs/weekly_points_df.csv", index_col="Owner")
st.header("Weekly player points")
st.dataframe(weekly_points_df)
