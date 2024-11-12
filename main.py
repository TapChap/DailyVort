import RecipientsAPI
import prompt, ParashaAPI, json
from GPTconfig import Prompt
from chatGPT import chatGPT
from sendEmail import sendEmail

def getDailyTorah(weekDay, parasha):
    return chatGPT(prompt.systemPrompt + Prompt("פרשת השבוע היא " + parasha) + prompt.Week().getPrompt(weekDay))

gmail_user = "shaigimel@gmail.com"
gmail_password = "xmbp rlzd pnst ciej"

def lambda_handler(event, context):
    parasha = ParashaAPI.getParasha()
    dayOfTheWeek = prompt.getWeekDay()
    # recipients = open('recipients.txt', 'r').read().splitlines()
    recipients = RecipientsAPI.getRecipients()

    if dayOfTheWeek == 7:
        return {
            'statusCode': 503,
            'body': json.dumps('unable to send email in Shabbat')
        }

    dailyTorah = getDailyTorah(dayOfTheWeek, parasha)
    sendEmail(gmail_user, gmail_password, recipients, "הפרשה היומית - chatGPT", dailyTorah + '\n\n generetad by chatGPT, sent by SMTP, built by Shai Grossman')

    return {'statusCode': 200}