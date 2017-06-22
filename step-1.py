if True:
    print('hello')
    print(' world!')

a = 'hello'
print(type(a))

a = 15
print(type(a))

a = True
print(a)
print(type(a))

matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))

print(matrix_t)

list_a = [1, 3, 5]
list_b = [2, 4, 6]
list_c = [100, 200, 300]

result = list(zip(list_a, list_b, list_c))
print(result)

result_2 = list(map(list, result))
print(result_2)
print("один элемент списка {}".format(result_2[1]))

print(*result_2)

print('*' * 20)
for element in result_2:
    print("\tодин элемент списка {}".format(element))

print('*' * 20)
for number, element in enumerate(result_2, 1):
    print("\tэлемент списка № {}: {}".format(number, element))


def summ(arg1, arg2):
    print('working')
    return arg1 + arg2


def summ_multi(*args):
    print('working')
    return sum(args)


print(summ(18, 25))
print(summ_multi(18, 25, 58, 95, 88, 190))

# PILLOW
# pip install pillow

# print(dir(matrix_t))

# print(help(matrix_t))

