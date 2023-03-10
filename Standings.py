import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Cric Talk Draft")
st.markdown("Summer Is Coming 2023")

standings_df = pd.read_csv("./Outputs/standings_df.csv", index_col="Owner")
cumsum_df = pd.read_csv("./Outputs/cumsum_df.csv", index_col="Owner")

col1, col2 = st.columns([2, 3])
# st.header("Standings")
# st.dataframe(standings_df)

# st.header("Draft Standings Race")
# st.line_chart(cumsum_df.T)

col1.subheader("Standings")
col1.dataframe(standings_df)

col2.subheader("Draft Standings Race")
col2.line_chart(cumsum_df.T)
