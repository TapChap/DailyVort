from GPTconfig import *

instruct1 = Prompt("תתפקד בתור רב, שמומחה בפרשת השבוע", Role.SYSTEM)
instruct2 = Prompt("תכתוב דבר תורה קצר *ומקורי* על הפרשה שיספק לך המשתמש", Role.SYSTEM)
instruct3 = Prompt(f"דבר התורה צריך להיות באורך של עשרה משפטים", Role.SYSTEM)

systemPrompt = Conversation(instruct1, instruct2, instruct3)
from GPTconfig import *
import datetime

instruct1 = Prompt("תתפקד בתור רב, שמומחה בפרשת השבוע", Role.SYSTEM)
instruct2 = Prompt("תכתוב דבר תורה קצר *ומקורי* על הפרשה שיספק לך המשתמש", Role.SYSTEM)
instruct3 = Prompt(f"דבר התורה צריך להיות באורך של עשרה משפטים", Role.SYSTEM)

systemPrompt = Conversation(instruct1, instruct2, instruct3)

class Week:
    SUNDAY = Prompt("ספר את הסיפור של פרשת השבוע בשפה פשוטה וקלה להבנה, מבלי להיכנס לפרשנויות מעמיקות. הסבר את השתלשלות האירועים ואת המסר המרכזי שהפרשה מעבירה, בדומה לסיכום פשט.")
    MONDAY = Prompt("בהנחה שהקורא כבר מכיר את פשט פרשת השבוע, תוסיף תובנות ופרטים מעניינים שמעשירים את הסיפור. הוסף ניתוחים קלים לדמויות ולאירועים המרכזיים בפרשה, תוך הדגשת פרטים שיכולים להפתיע או להעמיק את ההבנה.")
    TUESDAY = Prompt('תאר את הסיפור המרכזי של פרשת השבוע והסבר פרשנות בסיסית של רש"י על הפסוקים המרכזיים. ציין פרשנויות פשוטות נוספות שנותנות עומק נוסף לפשט')
    WEDNESDAY = Prompt("במהלך פרשת השבוע ישנם לקחים ומסרים שניתן ללמוד מהסיפור. הצג מסר או מוסר השכל עיקרי שניתן להסיק מהפרשה. הדגם כיצד לקח זה יכול להיות רלוונטי לחיים היום.")
    THURSDAY = Prompt("פרט על פרשת השבוע תוך שילוב פרשנויות מעמיקות יותר כמו אלו של הרמבן או אבן עזרא. הסבר מושגים או נושאים מהותיים בפרשה שמתייחסים לעקרונות רוחניים ומוסריים עמוקים יותר.")
    FRIDAY = Prompt(
        'בפרשת השבוע ישנם נושאים ועומקים נסתרים מעבר לפשט. הצג דמות או רעיון מרכזי והסבר ניתוח מעמיק מפרשן כמו רבי צדוק הכהן מלובלין או המהר"ל מפראג. העלה תובנות ייחודיות, רעיונות פילוסופיים או תכנים חבויים אחרים.')

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