import streamlit as st
import pandas as pd
import altair as alt
from helpers import read_file

st.set_page_config(page_title="Plots", page_icon="📊")

st.markdown("# Comparison plots")

bucket_name = "summer-is-coming-2023"
cumsum_df = read_file(bucket_name, "Outputs/cumsum_df.csv").set_index("Owner")

players = st.multiselect("Choose players", cumsum_df.index)
if not players:
    st.error("Please select at least one player")
else:

    data = cumsum_df.loc[players]
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "Match", "value": "Cumulative Points"}
    )

    chart = (
        alt.Chart(data)
        .mark_line()
        .encode(x="Match", y="Cumulative Points", color="Owner")
    )

    st.altair_chart(chart, use_container_width=True)
