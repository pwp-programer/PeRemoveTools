from datetime import  datetime
import os, random, shutil, win10toast, winshell


# Block of functions
def func_clear_recycle_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)


def func_clear_temp(temp_path):
    shutil.rmtree(temp_path, ignore_errors=True)


def func_info_message(bin_logo):
    print(bin_logo)


def func_notification_message(toast, why, mode):
    if mode == "error":
        toast.show_toast(title="PyRemoveTools", msg=f"Возникла ошибка при очистке {why}", duration=4)
    elif mode == "complete":
        toast.show_toast(title="PyRemoveTools", msg=f"{why} успешно очищена", duration=4)




# Important variables
user_name = "pwp"
temp_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Temp"
toast = win10toast.ToastNotifier()




try:
    settings_file = open("C:\\test\\configure.txt", "r+")
    date_with_file = []

    for i in settings_file:
        if i != "":
            date_with_file.append(int(i))

    d = datetime(date_with_file[0], date_with_file[1], date_with_file[2])


    some_date = datetime.now()

    if (some_date - d).days <= -2 or (some_date - d).days >= 2:
        try:
            func_clear_temp(temp_path)
            func_clear_recycle_bin()
            func_notification_message(toast, "Корзина и папка temp", "complete")
        except:
            func_notification_message(toast, "корзины и папки temp", "error")


        settings_file = open("C:\\test\\configure.txt", "w+")

        now_date = datetime.now()
        day = now_date.day
        month = now_date.month
        year = now_date.year

        settings_file.write(str(year) + "\n")
        settings_file.write(str(month) + "\n")
        settings_file.write(str(day))


except:
    settings_file = open("C:\\test\\configure.txt", "w+")

    now_date = datetime.now()
    day = now_date.day
    month = now_date.month
    year = now_date.year

    settings_file.write(str(year) + "\n")
    settings_file.write(str(month) + "\n")
    settings_file.write(str(day))
