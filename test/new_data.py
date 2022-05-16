from datetime import datetime


some_date = datetime(2022, 4, 29)
now_date = datetime.now()
# day = now_date.day
# month = now_date.month
# year = now_date.year



# print(day, month, year, sep=" ", end=" ")

a = (some_date - now_date).days

if (some_date - now_date).days == -3:
    print("clear")
