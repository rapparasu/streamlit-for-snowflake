
""""
show employees hierarchial data (dataframe, Graph and Dot Code) in tabs where the 
data from the uploaded file is cached across page run triggered by the input controls. 


streamlit run first_app\8_app_hierarchial_tabular_with_caching.py


"""
import urllib.parse
import pandas as pd
import streamlit as st
from io  import StringIO

def getGraph(df):
    edges = ""
    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
            edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'
    return f'digraph {{\n{edges}}}'

#use streamlit decorator cache_data to cache the data frame. 
# The data frame loaded from a static file, so there is no point in re-loading the datafram
# across page runs triggered by the input control events. 
@st.cache_data
def loadFile(filename):
    return pd.read_csv(filename, header=0).convert_dtypes()

st.title("Hierarchical Data Viewer")

filename = "first_app\data\employees.csv"


uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file", type=["csv"], accept_multiple_files=False)
if uploaded_file is not None:
    filename = StringIO(uploaded_file.getvalue().decode("utf-8"))


df_orig = loadFile(filename)
cols = list(df_orig.columns)

with st.sidebar:
    child = st.selectbox("Child Column Name", cols, index=0)
    parent = st.selectbox("Parent Column Name", cols, index=1)
    df = df_orig[[child, parent]]

tabs = st.tabs(["Source", "Graph", "Dot Code"])
tabs[0].dataframe(df_orig)

chart = getGraph(df)
tabs[1].graphviz_chart(chart, use_container_width=True)

url = f'http://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'
tabs[2].link_button("Visualize Online", url)
tabs[2].code(chart)

