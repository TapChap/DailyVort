from main import getWeeklyTorah, formatResponse, parasha

if __name__ == '__main__':
    file = open(f"./Torah/{parasha}.txt", 'w')

    file.write("דברי תורה לפרשת: " + parasha + '\n')

    file.write("יום ראשון" + '\n')
    file.write(getWeeklyTorah(1, parasha))
    file.write(2 * '\n')

    file.write("יום שני" + '\n')
    file.write(getWeeklyTorah(2, parasha))
    file.write(2 * '\n')

    file.write("יום שלישי" + '\n')
    file.write(getWeeklyTorah(3, parasha))
    file.write(2 * '\n')

    file.write("יום רביעי" + '\n')
    file.write(getWeeklyTorah(4, parasha))
    file.write(2 * '\n')

    file.write("יום חמישי" + '\n')
    file.write(getWeeklyTorah(5, parasha))
    file.write(2 * '\n')

    file.write("יום שישי" + '\n')
    file.write(getWeeklyTorah(6, parasha))
    file.write(2 * '\n')

    print(file.read())

    file.close()