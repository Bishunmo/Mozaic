import os

dir_name = "nums"

images_list = os.listdir(dir_name)

print(images_list)

images_list_full_name = []

for fname in images_list:
    images_list_full_name.append(os.path.join(dir_name, fname))


print(images_list_full_name)

images_list_full_name_generator = [os.path.join(dir_name, fname) for fname in images_list]

print(images_list_full_name_generator)

a = 5
b = 7

c = a
a = b
b = c
# через кортежи - tuples
a, b, c = c, b, a

a = (b, c)