import streamlit as st
import pandas as pd
from settings import owner_team_dict
from helpers import read_file
from st_aggrid import AgGrid

bucket_name = "summer-is-coming-2023"

st.set_page_config(layout="wide")
for owner in sorted(owner_team_dict.keys()):
    st.header(owner)
    trade_df = read_file(
        bucket_name, "Trades.xlsx", format="excel", sheet_name=owner
    ).set_index("S.no")

    st.dataframe(trade_df)
    # AgGrid(trade_df)
