import streamlit as st
#header of app
st.header("Anurag University records")
#title of app
st.title("Welcome to Student Management")
#sub header of app
st.subheader("manage student records")
#horizontal line
st.markdown("--------")
#text method to display info
st.text("Student Info is here")
#to add extra info of any type
st.write("hello")
st.write(12345)
st.write({"name":"Sneha","age":20})
#to format text
st.markdown("### features of application:")
st.markdown("*Italic text*")
st.markdown("**Bold text**")
st.markdown("- item1\n- item2")
st.markdown("<p style='color:blue'>Blue</p>",unsafe_allow_html=True) 
#to add cation
st.caption("This is caption")   
#to add code snippet
st.code("""
        def add(a,b):
        return a+b""")
st.code("print('Hello World')")
#to add mathematical equations not solve
st.latex(r''' a^2 + b^2 = c^2 ''')
st.latex(r'''\int_{a}^{b} x^2 dx''')
st.latex(r'''\frac{a}{b} = c''')
#to add divider/horizontal line
st.divider()
#to display success message
st.success("Operation Successful")
#button creation
if st.button("Click Me"):
    st.write("Button Clicked")
    st.balloons()  
    st.snow()
else:
    st.write("Button Not Clicked")
#to input text from user st.ext_input
name=st.text_input("Enter your name")
if name=="":
    st.warning("Name is required")
elif not name.isalpha():
    st.error("Name should have only alphabets")
else:
    print(name)
#to input multi line text from user st.text_area
address=st.text_area("Enter your address")
#checkbox creation
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing")  
#radio button creation
st.radio("select your gender:",("male","female","other"))
#select keyword to create dropdown
course=st.selectbox("Select your course:",["B.Tech","M.Tech","MBA","BBA"])
st.write("Your course is",course)
#multi select creation
skills=st.multiselect("Select your skills:",["python","java","c"])
#slider to create slider
rating=st.slider("Select your rating:",0,100)
#upload files
st.file_uploader("Upload your file:")
#form creation
with st.form("My form"):
    name=st.text_input("Enter your name")
    age=st.number_input("Enter age",0,100)
    username=st.text_input("Enter username")
    password=st.text_input("Enter password",type="password")
    Login=st.form_submit_button("Login")
if Login:
    st.success("Login Successful")
#columns method to create multiple columns
col1,col2,col3=st.columns(3)
with col1:
    st.text("Name")
    st.write("Sneha")
with col2:
    st.text("Age")
    st.write("20")        
with col3:
    st.text("Roll No")
    st.write("06")
st.divider()
#to create container
container=st.container()
with container:
    st.header("This is inside the container")
    st.text("You can add multiple elements here")
st.divider()
#to create table
st.table({"Name":["Anurag","Sneha","Rohit"],"Age":[21,20,22],"Course":["B.Tech","MBA","M.Tech"]})
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
#to  create sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
st.divider()
st.sidebar.title("Home")
option=st.sidebar.selectbox("Choose page",["main course","dessert","drinks"])