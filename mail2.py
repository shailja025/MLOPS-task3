# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "shailjatripathi025@gmail.com"
# Receivers email
rec_email = "shailjatripathi025@gmail.com"

message = (""" The Accuracy Of uR MoDel is GoOod nOw u caN ProceeD FurThur ! """)

# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("shailjatripathi025@gmail.com", "1234")
print("Login Success!")
# Send Email
server.sendmail("Shailja Tripathi", "Email", message)
print(f"Email has been sent successfully to {rec_email}")
