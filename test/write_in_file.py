from datetime import  datetime

try:
    settings_file = open("configure.txt", "r")

except:
    settings_file = open("configure.txt", "w+")

    now_date = datetime.now()
    day = now_date.day
    month = now_date.month
    year = now_date.year

    settings_file.write(str(year) + "\n")
    settings_file.write(str(month) + "\n")
    settings_file.write(str(day))
