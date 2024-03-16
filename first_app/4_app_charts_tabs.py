
'''

represent employee hierarchial data in differen charts: Treemap, icicle, sunburst, sankey etc. 
These charts are rendered in different tabs. 

streamlit run first_app\4_app_charts_tabs.py

'''

import pandas as pd
import urllib.parse
import webbrowser
import streamlit as st
import plotly.graph_objects as go


#1. create a TreeMap chart for Hierachial data
def makeTreeMap(labels, parents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
        )
    fig = go.Figure(data)
    return fig

#2. create a Icicle chart for Hierachial data
def makeIcicile(labels,parents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
        )
    fig = go.Figure(data)
    return fig



#3. create a Sunburst chart for Hierachial data
def makeSunburst(labels,parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        insidetextorientation='horizontal'
        )
    fig = go.Figure(data)
    return fig


#4. create a Sankey chart for Hierachial data
def makeSankey(labels,parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
            label=labels,
            value=list(range(1, len(labels)))))
    fig = go.Figure(data)
    return fig  



#give a title for the streamlit app
st.title("Hierarchial Data Charts In Tabs")


df = pd.read_csv("first_app\data\employees.csv", header=0).convert_dtypes()

#st.dataframe(df)

labels, parents= df[df.columns[0]], df[df.columns[1]]

#tabular layout controls
t1,t2,t3,t4 = st.tabs(["Treemap", "Icicle", "Sunburst", "Sankey"])

with t1:
    fig =  makeTreeMap(labels,parents)
    #set container width to occupy the whole screen. 
    st.plotly_chart(fig, use_container_width=True)


with t2:
    fig =  makeIcicile(labels,parents)
    #set container width to occupy the whole screen. 
    st.plotly_chart(fig, use_container_width=True)

with t3:
    fig =  makeSunburst(labels,parents)
    #set container width to occupy the whole screen. 
    st.plotly_chart(fig, use_container_width=True)

with t4:
    fig =  makeSankey(labels,parents)
    #set container width to occupy the whole screen. 
    st.plotly_chart(fig, use_container_width=True)





