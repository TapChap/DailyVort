from GPTconfig import Prompt
import datetime

class Week:
    SUNDAY = Prompt("תכתוב בשפה פשוטה את מהלך הפרשה, על פי הפשט.")
    MONDAY = Prompt("תבחר שני נקודות מעניינות מהפרשה ותסביר אותם קצת יותר לעומק, מה בדיוק קורה בהן, תכנס קצת לפרטים")
    TUESDAY = Prompt("תחדש משהו מעניין על הפרשה שאינו ברור מייד מהפשט")
    WEDNESDAY = Prompt("תכתוב דבר תורה מעניין על הפשט, ברמה דיי בסיסית, תכניס קצת פרשנים")
    THURSDAY = Prompt("תכתוב דבר תורה *מקורי* על נקודה אחת מהפרשה, משהו מעניין שאנשים לא מכירים")
    FRIDAY = Prompt(
        "תיצור לי דבר תורה ברמה גבוהה מאוד, דבר תורה שמתאים לרבני ישראל להגיד בשולחן שבת, עם מסר חזק ומעניין")

    def getPrompt(self, num):
        match num:
            case 1:
                return self.SUNDAY
            case 2:
                return self.MONDAY
            case 3:
                return self.TUESDAY
            case 4:
                return self.WEDNESDAY
            case 5:
                return self.THURSDAY
            case 6:
                return self.FRIDAY


def getWeekDay():
    return (datetime.date.today().weekday() + 1) % 7 + 1