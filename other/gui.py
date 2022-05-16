from cProfile import label
from email.mime import message
from tkinter import *
# import win10toast
import winshell
import shutil
from tkinter import messagebox

# Инициализация функций
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def label_func(text):
    main_label_text = Label(text=f"{text}",
                            fg="white", bg=_from_rgb((5, 39, 59)), font="128")
    main_label_text.pack(side="bottom")



def func_clear_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
    except:
        print("error")

def func_clear_temp(temp_path):
    try:
        shutil.rmtree(temp_path, ignore_errors=True)
    except:
        print("error")


def all_clear_func(temp_path):
    try:
        func_clear_recycle_bin()
        func_clear_temp(temp_path)
    except:
        print("error")


# Инициализация функций связанных с гуи:
def main_text():
    main_label_text = Label(text="PyRemoveTools",
                            fg="white", bg=_from_rgb((5, 39, 59)), font="128")
    main_label_text.place(x=50, y=25, height=100, width=500)


def all_clear_button(temp_path):
    btn = Button(text="Очистить всё", command=all_clear_func(temp_path))
    btn.place(x=500,
            y=150,
            anchor="c",
            height=35,
            width=150,
            bordermode=OUTSIDE)


def clear_temp_button(temp_path):
        btn = Button(text="Очистить папку temp", command=func_clear_temp(temp_path))
        btn.place(x=300,
                y=150,
                anchor="c",
                height=35,
                width=150,
                bordermode=OUTSIDE)


def clear_recycle_bin_button():
    btn = Button(text="Очистить коризину", command=func_clear_recycle_bin())
    btn.place(x=100,
            y=150,
            anchor="c",
            height=35,
            width=150,
            bordermode=OUTSIDE)


# Пути
user_name = "pwp"
temp_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Temp"
gui = Tk()
gui.title("PyRemoveTools")
gui.geometry("600x400+500+100")
gui.configure(bg=_from_rgb((5, 39, 59)))

main_text()
all_clear_button(temp_path)
clear_temp_button(temp_path)
clear_recycle_bin_button()
gui.mainloop()
