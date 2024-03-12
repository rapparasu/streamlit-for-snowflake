"""
demonstate the session state behavior for button and toggle button. 
As long as you just click the button the streamlit knows that the button has been clicked. 
Howver when you click the toggle button the page refereshes
and the streamlit doesn't remember that the button has been clicked earlier. 
whereas with Toggle button the session state is saved even after the page refreshes. 

streamlit run first_app\11_app_buttons_session_state.py

"""

import streamlit as st
st.title("About session")

#session state will hold the state of input controls on the page. 
#for the very first run it will be empty because the controls are not created yet.
st.write(st.session_state)

#create a button and set the key/identifier as my-button
if st.button("Button", key="my-button"):
    st.write("You clicked!")

#observe the behavior that when the page refreshes after you click the toggle button
#the button state is set to off because  session state for button is stateless
if st.toggle("Toggle", key="my-toggle"):
    st.write("You toggled!")

st.write(st.session_state)




