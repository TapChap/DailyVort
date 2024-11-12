import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmail(sender, password, receivers, subject, message):
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    html_message = f"""
        <html>
            <body style="direction: rtl;">
                <p>{message.replace('\n', '<br>')}</p>
            </body>
        </html>
        """

    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)  # Join list of emails as a single string
    msg["Subject"] = subject
    msg.attach(MIMEText(html_message, "html"))

    # Send the email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
