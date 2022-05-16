from datetime import datetime

settings_file = open("configure.txt", "r")
date_with_file = []

for i in settings_file:
    if i != "":
        date_with_file.append(int(i))

d = datetime(date_with_file[0], date_with_file[1], date_with_file[2])


some_date = datetime(2022, 4, 28)


if (some_date - d).days == -3:
    print(True)
