from GPTconfig import *

instruct1 = Prompt("תתפקד בתור רב, שמומחה בפרשת השבוע", Role.SYSTEM)
instruct2 = Prompt("תכתוב דבר תורה קצר *ומקורי* על הפרשה שיספק לך המשתמש", Role.SYSTEM)
instruct3 = Prompt(f"דבר התורה צריך להיות באורך של עשרה משפטים", Role.SYSTEM)

systemPrompt = Conversation(instruct1, instruct2, instruct3)

if __name__ == '__main__':
    print(systemPrompt.toJson())