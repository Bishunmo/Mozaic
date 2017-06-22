
list1 = [0, 1, 2, 3, '1', 'hello', 15.55]

list1[3] = 15

list1 = 'hello world!'
print(list1)

# print(list1)
print(type(list1))
# print(list1[3])
# sample1 = zip([0, 1], [3, 4], [6, 7])
# print(list(sample1))


# Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
        [ 1, 0.5, 0, 0, 0],
        [ 1, 1, 0.5, 0, 0],
        [ 1, 1, 1, 0.5, 0],
        [ 1, 1, 1, 1, 0.5]]

#Транспонирование
matrix_t = list(zip(*matrix))

# Вывод матриц
print(matrix)
print(matrix_t)

list1 = [1, 21, 87, 97]

for element in list1:
    print('\tКвадраты элементов списка {}, кубы {}'.format(element ** 2, element ** 3))
    print('\t\tЭлемент списка {}, ??? {}'.format(element, element // 3))

print('Всего выведено {}'.format(len(list1)))

print(dir('str'))

# pip install pillow

# for _element in list_current_dir:
#     print(choice(list_current_dir))

# [print(choice(list_current_dir)) for _element in list_current_dir]
# [print(_element) for _element in list_current_dir]

# [print(_element, choice(list_current_dir)) for _element in range(1, 5)]
# sample2 = range(1, 5)
# print(list(sample2))

def print_odd(max_num=10):
    for _num in range(1, max_num + 1):
        if _num % 2 == 0:
            print(_num)
        print('шаг')
    print('Цикл выполнен')
    print('*' * 20)

print_odd(15)
print_odd(5)

import os
list_current_dir = os.listdir('nums')

# for _element in list_current_dir:
#     print(os.path.join('nums', _element))
#     # print('\tnums\\{}'.format(_element))

# import this


# def print_list(argument):
#     print('список', argument)
#
# tesy_list = [1, 2, 'hello', 15, 15.5, 'sdfsdf']
# # print_list(tesy_list)
# #
# # abc = lambda x: print('список', x)
# #
# # abc(tesy_list)


# print(tesy_list[-1])
#
# print(tesy_list[len(tesy_list) - 1])
#
# a = 5
# b = 7
# print(a, b)
#
# c = a
# a = b
# b = c
# print(a, b)
#
# a, b = b, a
# print(a, b)
#
#  # map()
#  # sorted()