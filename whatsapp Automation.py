import pywhatkit as kit


# Parameters:
   # phone number (with country code, e.g., "+1234567890")
   # message
   # hour (24-hour format)
   # minute

phone_number = "+919550787234"
message = "Hello, this is an automated message!"
hour = 15 # 10 PM
minute = 15
try:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as e:
       print(f"An error occurred: {e}")


# In[ ]:




