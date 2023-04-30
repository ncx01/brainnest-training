''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase

# MIMEText() objects will contain the HTML and plain-text versions of the message
from email.mime.text import MIMEText

# MIMEMultipart("alternative") instance combines these into a single message with two alternative rendering options
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body, filename, sender, recipients, password):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    msg.attach(part)
    text = msg.as_string()

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

subject = "Multipart Test"

body = "This is an email with an attachment sent from Python"

filename = "document.pdf"

# Your email address
sender = "sender@gmail.com" 

# Your email password, should use input as it is not safe to store inside code, can import getpass module and
# use getpass() for blind input
password = input("Type your password and press enter: ")

recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]

send_email(subject, body, filename, sender, recipients, password)