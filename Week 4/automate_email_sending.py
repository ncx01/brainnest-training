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

import schedule
import time
from datetime import datetime

def send_email(subject, body, filePath, sender, recipient, password):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filePath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    filename = filePath.split('\\')[-1]
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    msg.attach(part)
    

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())

    writeLog(msg.as_string())

def sendReports():
    for filename in os.listdir(reportDirectory):
        filePath = os.path.join(reportDirectory, filename)
        print(filePath)
        for recipient in recipients:
            send_email(subject, body, filePath, sender, recipient, password)

def writeLog(text):
    now = datetime.now()
    logPath = os.path.join(currentDirectory, 'logs', 'log.txt')
    file = open(logPath, "a")
    file.write(now.strftime("%d/%m/%Y %H:%M:%S\n") + text)
    file.close()
    

subject = "Daily Report"
body = "This is an email with an attachment sent from Python"

# Your email address
sender = "nicholascos@gmail.com" 

# Your email password, should use input as it is not safe to store inside code, can import getpass module and
# use getpass() for blind input
password = 'reycaprarijynehk'#'01%Hawking04' # input("Type your password and press enter: ")
recipients = ["antonio.cosentino@proton.me", "nicholas.cosentino@proton.me"]
currentDirectory = os.path.dirname(os.path.realpath(__file__))
reportDirectory = os.path.join(currentDirectory, 'Reports')

schedule.every().day.at("22:59").do(sendReports)

while True:
    schedule.run_pending()
    time.sleep(1)