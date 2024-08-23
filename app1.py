import pywhatkit
import streamlit as st
from datetime import datetime
phonelist = st.text_input("Please input numbers you want to automate with seperated by ,")
message = st.text_area("Enter your Message")
submit = st.button("Enter")

phone_number = "+919550787234"
message = "Hello, this is an automated message!"
hour = 19 # 11 PM
minute = 10
try:
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as e:
       print(f"An error occurred: {e}")
st.success("Message Sent!")