''''
represent hierarchial data as digraph. 

as the code contains streamlit, you will need to run the below python file:
streamlit run first_app\app_digraph.py

run the below command to see their demo project and look at their code. 
streamlit hello

'''
import pandas as pd
import urllib.parse
import webbrowser
import streamlit as st

#give a title for the streamlit app
st.title("Hierarchial Data Viewer")

df = pd.read_csv("first_app\data\employees.csv", header=0).convert_dtypes()
#print(df)
st.dataframe(df)

edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph{{\n{edges}}}'  

st.graphviz_chart(d)










