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
main_window.title("game 15")

# список объектов-картинок
image_objects_list = [tkinter.PhotoImage(file=_image) for _image in images_list_full_name]

labels = []

for num_row, _image in enumerate(image_objects_list):
    label = tkinter.Label(main_window, image=_image)
    label.grid(row=num_row, column=0)

    labels.append(label)


def keypress(arg):
    print(arg)

main_window.bind('<Up>', lambda x: print(x))
main_window.bind('<Down>', keypress)
main_window.bind('<Left>', keypress)
main_window.bind('<Right>', keypress)
main_window.bind('<q>', lambda x: exit(0))


main_window.mainloop()