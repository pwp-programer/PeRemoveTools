from logo import bin_logo
import cowsay, os, random, shutil, win10toast, winshell


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

value_choice = input(
    '''
1 - Очистка корзины
2 - Очистка папки temp
3 - Очистка всего сразу

''')

toast = win10toast.ToastNotifier()



# The starting point of the program
if __name__ == "__main__":
    if value_choice == "1":
        try:
            func_clear_recycle_bin()
            func_notification_message(toast, "Корзина", "complete")
        except:
            func_notification_message(toast,
                                "корзины, попробуйте снова\nВозможно корзина уже пуста, проверьте перед очисткой...",
                                "error")

    elif value_choice == "2":
        try:
            func_clear_temp(temp_path)
            func_notification_message(toast, "Папка temp", "complete")
        except:
            func_notification_message(toast, "temp", "error")

    elif value_choice == "3":
        try:
            func_clear_temp(temp_path)
            func_clear_recycle_bin()
            func_notification_message(toast, "Корзина и папка temp", "complete")
        except:
            func_notification_message(toast, "корзины и папки temp", "error")

    elif value_choice == "info":
        func_info_message(bin_logo)
