'''
represent employee hierarchial data in differen charts: Treemap, icicle, sunburst, sankey etc. 

streamlit run first_app\3_app_charts.py

'''

import pandas as pd
import urllib.parse
import webbrowser
import streamlit as st
import plotly.graph_objects as go

#give a title for the streamlit app
st.title("Hierarchial Data Charts")

df = pd.read_csv("first_app\data\employees.csv", header=0).convert_dtypes()

#st.dataframe(df)

labels = df[df.columns[0]]
parents = df[df.columns[1]]

#1. create a TreeMap chart for Hierachial data
data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"

)

fig = go.Figure(data)

#set container width to occupy the whole screen. 
st.plotly_chart(fig, use_container_width=True)

#2. create a Icicle chart for Hierachial data
data = go.Icicle(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color="lightgray"

)

fig = go.Figure(data)

#set container width to occupy the whole screen. 
st.plotly_chart(fig, use_container_width=True)

#3. create a Sunburst chart for Hierachial data
data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal'

)

fig = go.Figure(data)

#set container width to occupy the whole screen. 
st.plotly_chart(fig, use_container_width=True)

#4. create a Sankey chart for Hierachial data
data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)

