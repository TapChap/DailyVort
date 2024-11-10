import json
import prompt, ParashaAPI, WeekDaysPrompt
from GPTconfig import Prompt
from chatGPT import chatGPT
from sendEmail import sendEmail

def getDailyTorah(weekDay, parasha):
    return chatGPT(prompt.systemPrompt + Prompt("פרשת השבוע היא " + parasha) + WeekDaysPrompt.Week().getPrompt(weekDay))

gmail_user = "shaigimel@gmail.com"
gmail_password = "xmbp rlzd pnst ciej"

def lambda_handler(event, context):
    parasha = ParashaAPI.getParasha()
    dayOfTheWeek = WeekDaysPrompt.getWeekDay()

    if dayOfTheWeek == 7:
        return {
            'statusCode': 500,
            'body': json.dumps('unable to send email in Shabbat')
        }

    dailyTorah = getDailyTorah(dayOfTheWeek, parasha)
    sendEmail(gmail_user, gmail_password, ["shaigimel@gmail.com", "grossmaneph@gmail.com", "Shalev223344@gmail.com"], "Daily Torah", dailyTorah)

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('success.')
    # }
