import streamlit as st
import pandas as pd
from settings import owner_team_dict
from st_aggrid import AgGrid

st.set_page_config(layout="wide")
for owner in sorted(owner_team_dict.keys()):
    st.header(owner)
    trade_df = pd.read_excel("Trades.xlsx", sheet_name=owner, index_col="S.no")
    st.dataframe(trade_df)
    # AgGrid(trade_df)
