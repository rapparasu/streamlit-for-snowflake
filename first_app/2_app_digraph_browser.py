
"""
represent the hierarchial data for employees.csv by contructing a digraph and opening that in a browser

streamlit run first_app\2_app_digraph_browser.py

"""
import pandas as pd
import urllib.parse
import webbrowser

df = pd.read_csv("first_app\data\employees.csv", header=0).convert_dtypes()
print(df)

edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph{{\n{edges}}}'  
print(d)  

'''

now open the graphviz visual editor 
http://magjac.com/graphviz-visual-editor/
paste the d value from print statement to visualize the hierarchial data.

'''

#or alternatively you can open the graphviz editor in browser programatically as below. 
url = f'http://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(d)}'
webbrowser.open(url)









