'''
this python fils shows the basic list of streamlit methods available
streamlit run first_app\7_app_streamlit_functions.py

'''

import streamlit as st

st.title("Hierarchial Data Viewer")
st.header("This is a header")
st.subheader("subheader")
st.caption("caption")

st.write("this is write")
st.text("fixed text")
st.code("v=variable()\nanother_call()", "python")
#2 starts is bold and 1 is italic
st.markdown("**bold**")
st.markdown("*italic*")

st.divider()
st.latex(".....")
st.error("This is an error")
st.info("This is an info")
st.warning("This is a warning")
st.success("This is success")

st.balloons()
st.snow()
