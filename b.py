
import time
from login import login_user
from mysql.connector import Error
import streamlit as st
import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="streamlit_appp"

)
st.markdown("<h1 style='text-align: center; color: #667eea;'>🔐 Student Portal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Login or Register to Continue</p>", unsafe_allow_html=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Register", "Login"])
if page == "Register":
    with st.form("My Form"):
     st.header("Student Registration Form")
     name=st.text_input("Enter your name")
     age=st.number_input("Enter age",0,100)
     gender=st.radio("Select your gender:",("male","female","other")) 
     email=st.text_input("Enter your email")   
     username=st.text_input("Enter username")
     password=st.text_input("Enter password",type="password")
     Submit=st.form_submit_button("Submit")
    if Submit:
        conn=None
        cursor=None
        try:
            conn=get_connection()
            cursor=conn.cursor()

            cursor.execute("Insert into user_info(name,age,gender,email,username,password) "
        "values(%s,%s,%s,%s,%s,%s)",(name,age,gender,email,username,password) )
            conn.commit()
            st.success("Form Submitted Successfully!Go to login page to login")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
        finally:
         if cursor:
            cursor.close()
         if conn:
            conn.close()    
if page == "Login":
    def login_user(username,password):
        conn=None
        cursor=None
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("Select * from user_info where username=%s and password=%s",(username,password))
            result=cursor.fetchone()
            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    st.header("User Login")
    username=st.text_input("Enter username")
    password=st.text_input("Enter password",type="password")
    if st.button("Login"):
        if login_user(username,password):
            st.success("Login Successful!")
            st.balloons()
        else:
            st.error("Login Failed. Please check your credentials.")

def create_user_info_table():
    pass

def main():
    # Create users table on app startup
    create_user_info_table()
    
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center; color: #667eea;'>🔐 Student PortalS</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>Login or Register to Continue</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main content area
    if st.session_state.get("logged_in", False):
        mode = st.sidebar.selectbox("Select Mode", ["🏠 Home", "👤 Profile", "📊 Dashboard", "⚙️ Settings", "🚪 Logout"])

        # Header Navigation
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        with col1:
            if st.button("🏠 Home", use_container_width=True, key="nav_home"):
                st.session_state.page = "home"
        with col2:
            if st.button("👤 Profile", use_container_width=True, key="nav_profile"):
                st.session_state.page = "profile"
        with col3:
            if st.button("📊 Dashboard", use_container_width=True, key="nav_dashboard"):
                st.session_state.page = "dashboard"
        with col4:
            if st.button("⚙️ Settings", use_container_width=True, key="nav_settings"):
                st.session_state.page = "settings"
        with col5:
            if st.button("🚪 Logout", use_container_width=True, key="logout_btn"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.success("✅ Logged out successfully!")
                time.sleep(1)
                st.rerun()
        
        st.markdown("---")

if __name__ == "__main__":
    main()



