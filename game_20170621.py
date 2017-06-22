# https://yadi.sk/d/bhwJI7M03JFmij - картинки к игре
# https://yadi.sk/i/cwbB1zai3JdmDC - начало игры

# Подключение модулей
import os, tkinter, random


# # Модуль tkinter - для создания GUI
#
# # from tkinter import Tk, Label, Button
# from random import choice
#
# # PEP 8
# # Для работы с графикой воспользуемся дополнительной библиотекой - PIL
# # Необходимо установить библиотеку Pillow:  pip install Pillow
# from PIL import Image, ImageTk
#
# SIDE = 4  # <- величина стороны квадрата (для пятнашек квадрат 4х4)
#
# IMG_DIR = 'images'
#

dir_name = "nums"

images_list = os.listdir(dir_name)

images_list_full_name = [os.path.join(dir_name, fname) for fname in images_list]

random.shuffle(images_list_full_name)

main_window = tkinter.Tk()
# print(type(main_window))

main_window.title("game 15")

label_1 = tkinter.Label(main_window, text="Hello, world!")
# label_1.pack()
label_1.grid(row=0, column=0)


image_1 = tkinter.PhotoImage(file=images_list_full_name[2])
label_2 = tkinter.Label(main_window, image=image_1)
label_2.grid(row=1, column=0)


def keypress(arg):
    print(arg)

main_window.bind('<Up>', lambda x: print(x))
main_window.bind('<Down>', keypress)
main_window.bind('<Left>', keypress)
main_window.bind('<Right>', keypress)
main_window.bind('<q>', lambda x: exit(0))


main_window.mainloop()