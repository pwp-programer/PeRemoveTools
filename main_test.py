import cowsay
import os
import random
import shutil
import winshell
from logo import bin_logo


def func_info_message():
    print(bin_logo)


def func_clear_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print("Корзина очищена")
    except:
        print("Возникла ошибка при чистке корзины, попробуйте снова\nВозможно корзина уже пуста, проверьте перед очисткой...")


def func_delete_folder(path):
    # folder_name = input("Введите имя папки для удаления: ")
    # folder_path = input("Введите путь для удаления папки: ")
    try:
        shutil.rmtree(f'{path}')
        # shutil.rmtree(f'{folder_path}\\{folder_name}')
        print("Папка удалена")
    except:
        print("При удалении папки возникла ошибка, попробуйте ещё раз...")


def func_clear_temp(temp_path):
    try:
        shutil.rmtree(temp_path, ignore_errors=True)
        print("Папка temp очищена")
    except:
        print("Возникла ошибка при очистки папки temp...")


user_name = "pwp"
test_path = f"C:\\Users\\{user_name}\\Documents\\my file\\test"
temp_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Temp"

value_choice = input(
    "1 - чистка корзины, 2 - чистка папки темп, 3 - удаление папки: ")

if __name__ == "__main__":
    if value_choice == "1":
        func_clear_recycle_bin()

    elif value_choice == "2":
        func_clear_temp(temp_path)

    elif value_choice == "3":
        func_delete_folder(test_path)

    elif value_choice == "info":
        func_info_message()

    else:
        func_info_message()
