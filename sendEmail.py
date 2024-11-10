import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import time

def lambda_handler(event, context):

    local_time = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

    gmail_user = "shaigimel@gmail.com"
    gmail_password = "xmbp rlzd pnst ciej"

    sendEmail(gmail_user, gmail_password, "shaigrossman14@gmail.com", "timeTest",
              f"this Gmail was sent at: {current_time}")

    return {
        'statusCode': 200,
        'body': json.dumps('sent mail')
    }

def sendEmail(sender, password, receiver, subject, massage):
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(massage, "plain"))

    # Send the email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
