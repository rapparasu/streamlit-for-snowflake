
""""
show employees hierarchial data (dataframe, Graph and Dot Code) in tabs where the 
data from the uploaded file is cached across page runs triggered by the input controls
and the filename that was uploaded is loaded into the session state. The code checks if the uploaded
file is portfolio.csv then it throws an error. This is done using callback functionality. 

streamlit run first_app\10_app_hierarchial_tabular_with_Callback.py


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


#callback method for button onclick event. 
def OnShowList(filename):
    if "names" in st.session_state:
        filenames = st.session_state["names"]
        if filename in filenames:
            st.error("Critical file found!")
            st.stop()

#use streamlit decorator cache_data to cache the data frame. 
# The data frame loaded from a static file, so there is no point in re-loading the datafram
# across page runs triggered by the input control events. 
@st.cache_data
def loadFile(filename):
    return pd.read_csv(filename, header=0).convert_dtypes()

st.title("Hierarchical Data Viewer")

if "names" in st.session_state:
    filenames = st.session_state["names"]
else:
    #default the filenames to employee.csv
    filenames = ["employees.csv"]
    st.session_state["names"] = filenames


filename = "first_app\data\employees.csv"

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file", type=["csv"], accept_multiple_files=False)
if uploaded_file is not None:
    filename = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #get the actual name of the uploaded file
    file = uploaded_file.name
    if file not in filenames:
        filenames.append(file)


#create a button and attach an onclick event. args accepts a tuple, so default it to portfolio.csv
btn = st.sidebar.button("Show List",
                        on_click = OnShowList, args=("portfolio.csv",))

#show the uploaded filel list only when the button is clicked. 
if btn:
    for f in filenames:
        st.sidebar.write(f)


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

