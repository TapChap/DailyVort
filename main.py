import prompt, ParashaAPI, json, RecipientsAPI
from GPTconfig import Prompt
from chatGPT import chatGPT
from sendEmail import sendEmail

def getDailyTorah(weekDay, parasha):
    return chatGPT(prompt.systemPrompt + Prompt("פרשת השבוע היא " + parasha) + prompt.Week().getPrompt(weekDay)[0])

gmail_user = "shaigimel@gmail.com"
gmail_password = "xmbp rlzd pnst ciej"

def lambda_handler():
    parasha = ParashaAPI.getParasha()
    weekDay = prompt.getWeekDay()
    # recipients = open('recipients.txt', 'r').read().splitlines()
    recipients = RecipientsAPI.getRecipients()

    if weekDay == 7:
        return {
            'statusCode': 503,
            'body': json.dumps('unable to send email in Shabbat')
        }

    dailyTorah = getDailyTorah(weekDay, parasha)
    lineSpacing = '\n\n'
    emailSignature = 'generetad by chatGPT, built by Shai Grossman'

    subject = "הפרשה היומית - יום " + prompt.Week().getPrompt(weekDay)[1]
    massage = dailyTorah + lineSpacing + emailSignature

    print(dailyTorah)
    sendEmail(gmail_user, gmail_password, recipients, subject, massage)

    return {'statusCode': 200}

if __name__ == '__main__':
    lambda_handler()