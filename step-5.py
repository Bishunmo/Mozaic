# https://yadi.sk/d/bhwJI7M03JFmij - картинки к игре
# https://yadi.sk/i/cwbB1zai3JdmDC - начало игры

# Подключение модулей
import os, tkinter, random
from PIL import Image, ImageTk

dir_name = "nums"
SIDE = 4
images_list = os.listdir(dir_name)
moves = 0


def label_above(curr):
    ''' Вернуть соседа сверху
    '''
    return labels[(curr.row - 1) * SIDE + curr.column]


def label_under(curr):
    ''' Вернуть соседа снизу
    '''
    return labels[(curr.row + 1) * SIDE + curr.column]


def label_left(curr):
    ''' Вернуть соседа слева
    '''
    return labels[curr.row * SIDE + curr.column - 1]


def label_right(curr):
    ''' Вернуть соседа справа
    '''
    return labels[curr.row * SIDE + curr.column + 1]


def render(curr, near):
    ''' Отрисовка расположения двух клеток
    '''
    # if near is not None:
    if near:
        curr.grid(row=curr.row, column=curr.column)
        near.grid(row=near.row, column=near.column)


def exchange(curr, near):
    ''' Обмен местами клеток в общем списке
    '''
    # if near is not None:
    if near:
        ci = curr.row * SIDE + curr.column
        ni = near.row * SIDE + near.column
        labels[ci], labels[ni] = labels[ni], labels[ci]


def key_press(btn):
    ''' Основная логика перемещения на игровом поле.
        Основной элемент логики - пустая клетка - от неё определяем соседа.
        Потом меняем координаты пустой клетки и соседа.
    '''
    near = None  # <- None - специальное значение в Питоне - "ничто"
    # print(btn)
    global moves
    moves += 1

    if btn == 'r' and curr.column > 0:
        # print('Вправо')
        near = label_left(curr)
        curr.column -= 1
        near.column += 1
    elif btn == 'l' and curr.column < SIDE - 1:
        # print('Влево')
        near = label_right(curr)
        curr.column += 1
        near.column -= 1
    elif btn == 'u' and curr.row < SIDE - 1:
        # print('Вверх')
        near = label_under(curr)
        curr.row += 1
        near.row -= 1
    elif btn == 'd' and curr.row > 0:
        # print('Вниз')
        near = label_above(curr)
        curr.row -= 1
        near.row += 1

    exchange(curr, near)
    render(curr, near)


def mix_up():
    ''' Перемешивание клеток
        SIDE ** 4 - взято для лучшего перемешивания,
         т.к. не все вызовы функции нажатия кнопок
         будут приводить клеток к движению на поле
    '''
    buttons = ['d', 'u', 'l', 'r']
    for i in range(SIDE ** 4):
        x = random.choice(buttons)  # <- choice - функция из модуля random
        # print('ход {}: {}'.format(i, x))
        key_press(x)


def get_regions(image):
    ''' Функция разбиения изображения на квадратики.
        На входе ожидает объект PIL.Image
        Возвращает список картинок-квадратиков ImageTk.PhotoImage
    '''
    regions = []
    pixels = image.width // SIDE
    for i in range(SIDE):
        for j in range(SIDE):
            x1 = j * pixels
            y1 = i * pixels
            x2 = j * pixels + pixels
            y2 = i * pixels + pixels
            box = (x1, y1, x2, y2)
            region = image.crop(box)
            region.load()
            regions.append(ImageTk.PhotoImage(region))
    return regions


images_list_full_name = [os.path.join(dir_name, fname) for fname in images_list]
# random.shuffle(images_list_full_name)


main_window = tkinter.Tk()
main_window.title("game 15")

# список объектов-картинок
# image_objects_list = [tkinter.PhotoImage(file=_image) for _image in images_list_full_name]

image = Image.open('test.jpg')
image_objects_list = get_regions(image)

print(image_objects_list)

labels = []

for i in range(SIDE):
    for j in range(SIDE):
        # переход от 2D в 1D
        x = i * SIDE + j
        label = tkinter.Label(main_window, image=image_objects_list[x])
        label.grid(row=i, column=j)
        # дополнительные атрибуты объекта label
        label.row = i
        label.column = j
        label.x = x

        labels.append(label)

curr = labels[-1]

main_window.bind('<Up>', lambda x: key_press('u'))
main_window.bind('<Down>', lambda x: key_press('d'))
main_window.bind('<Left>', lambda x: key_press('l'))
main_window.bind('<Right>', lambda x: key_press('r'))
main_window.bind('<q>', lambda x: exit(0))


# mix_up()
main_window.after(2000, mix_up)

main_window.mainloop()
