import RecipientsAPI
from sendEmail import sendEmail

recipients = RecipientsAPI.getRecipients()
gmail_user = "shaigimel@gmail.com"
gmail_password = "xmbp rlzd pnst ciej"

subject = ''
message = '''

'''

sendEmail(gmail_user, gmail_password, recipients, subject, message)
