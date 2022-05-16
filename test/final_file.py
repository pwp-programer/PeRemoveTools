from datetime import  datetime

try:
    settings_file = open("configure.txt", "r")
    settings_file = open("configure.txt", "r")
    date_with_file = []

    for i in settings_file:
        if i != "":
            date_with_file.append(int(i))

    d = datetime(date_with_file[0], date_with_file[1], date_with_file[2])


    some_date = datetime(2022, 4, 28)


    if (some_date - d).days == -3:
        print(True)


except:
    settings_file = open("configure.txt", "w+")

    now_date = datetime.now()
    day = now_date.day
    month = now_date.month
    year = now_date.year

    settings_file.write(str(year) + "\n")
    settings_file.write(str(month) + "\n")
    settings_file.write(str(day))
