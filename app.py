import streamlit as st
import requests

st.set_page_config(page_title="JobScout", layout="wide")

st.title("JobScout")
st.text(
    "JobScout is a web application that simplifies job searching by querying multiple job listing sites and saving "
    "user-defined searches. Utilizing a distributed work scheduler, it regularly updates the job listings database "
    "and notifies users of new opportunities. The application also features a user-friendly web interface for "
    "manual queries and real-time results."
)

job_title = st.text_input("Job Title:")
states = ['', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
          'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
          'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming']
location = st.selectbox(label="Location:", options=states)
company = st.text_input("Company:")

login_url = "http://localhost:5000/login"
logout_url = "http://localhost:5000/logout"
is_logged_in_url = "http://localhost:5000/is_logged_in"

if 'button_login_pressed' not in st.session_state:
    st.session_state.button_login_pressed = False

# Function to check login status
def check_login_status():
    response = requests.get(is_logged_in_url)
    if response.status_code == 200:
        data = response.json()
        st.session_state.button_login_pressed = data['logged_in']

# Function to handle login press
def handle_button_login_press():
    st.session_state.button_login_pressed = True
    st.markdown(f'<meta http-equiv="refresh" content="0; url={login_url}">', unsafe_allow_html=True)
    check_login_status()

# Function to handle logout press
def handle_button_logout_press():
    st.session_state.button_login_pressed = False
    st.markdown(f'<meta http-equiv="refresh" content="0; url={logout_url}">', unsafe_allow_html=True)

# Sidebar for floating menu
with st.sidebar:
    #st.header("Menu")
    # Display buttons based on the session state
    if not st.session_state.button_login_pressed:
        if st.button("Login with Google"):
            handle_button_login_press()
    else:
        if st.button("Logout"):
            handle_button_logout_press()

if st.button("Search"):
    # Handle job search logic here
    pass
