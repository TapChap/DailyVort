import prompt, ParashaAPI, WeekDaysPrompt
from GPTconfig import Prompt
from chatGPT import chatGPT

systemPrompt = prompt.systemPrompt
parasha = ParashaAPI.getParasha()
dayOfTheWeek = WeekDaysPrompt.getWeekDay()

def getWeeklyTorah(weekDay, parasha):
    return chatGPT(systemPrompt + Prompt("פרשת השבוע היא " + parasha) + WeekDaysPrompt.Week().getPrompt(weekDay))

# split each sentence to a new line
def formatResponse(response):
    formatted = ''
    response = response.split('.')

    for line in response:
        formatted += line
        formatted += '\n'

    return formatted

if __name__ == '__main__':
    print(formatResponse(getWeeklyTorah(dayOfTheWeek, parasha)))
