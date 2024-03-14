import hmac
import streamlit as st

#option1
def check_password():

    def password_entered():
        #read password from password key in .streamlit\secrets.toml
        #ensure to list this file in gitignore so that the file is not published. 
        if hmac.compare_digest(
            st.session_state["password"],
            st.secrets["password"]):
                st.session_state["password_correct"] = True
                del st.session_state["password"]
        else:
            st.session_state["password"] = False


    if not st.session_state.get("password_correct", False):
          st.text_input("Password", type="password", 
                        on_change=password_entered, key="password")
          
          if "password_correct" in st.session_state:
                st.error("Password incorrect")

          st.stop()

#option2
def check_user_and_password():
      
      def password_entered():
            #read the passswords from password section in .streamlit\secrets.toml
            if(st.session_state["username"] in st.secrets["passwords"]
               and hmac.compare_digest(st.session_state["password"],
                st.secrets.passwords[st.session_state["username"]])):
                st.session_state["password_correct"] = True
                del st.session_state["password"]
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False 


      def login_form():
            with st.form("Credentials"):
                  st.text_input("Username", key="username")
                  st.text_input("Password", type="password", key="password")
                  st.form_submit_button("Log in", on_click=password_entered)

      if not st.session_state.get("password_correct", False):
            login_form()
            if "password_correct" in st.session_state:
                  st.error("Password incorrect")
            st.stop()
            





