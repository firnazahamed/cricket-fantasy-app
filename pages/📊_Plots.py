import streamlit as st
import pandas as pd
import altair as alt
from helpers import read_file

st.set_page_config(page_title="Plots", page_icon="📊")

bucket_name = "summer-is-coming-2023"
cumsum_df = read_file(bucket_name, "Outputs/cumsum_df.csv").set_index("Owner")
sum_df = read_file(bucket_name, "Outputs/sum_df.csv").set_index("Owner")

st.header("Draft Standings Race")
st.line_chart(cumsum_df.T)

st.header("Comparison plots")

players = st.multiselect("Choose team owners", cumsum_df.index)
if not players:
    st.error("Please select at least one team owner")
else:

    st.header("Match wise points chart")
    chart_data = sum_df.loc[players].T
    st.area_chart(chart_data)

    cumsum_data = cumsum_df.loc[players]
    cumsum_data = cumsum_data.T.reset_index()
    cumsum_data = pd.melt(cumsum_data, id_vars=["index"]).rename(
        columns={"index": "Match", "value": "Cumulative Points"}
    )

    chart = (
        alt.Chart(cumsum_data)
        .mark_line()
        .encode(x="Match", y="Cumulative Points", color="Owner")
    )

    st.header("Cumulative points")
    st.altair_chart(chart, use_container_width=True)
