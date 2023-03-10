import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Plots", page_icon="📊")

st.markdown("# Comparison plots")

cumsum_df = pd.read_csv("./Outputs/cumsum_df.csv", index_col="Owner")

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
