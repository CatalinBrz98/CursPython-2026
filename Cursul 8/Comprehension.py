from time import time

# lista_nr = [1, 4, 6, 1, 2, 9, 100]
#
# # lista_paritate = []
# # for n in lista_nr:
# #     lista_paritate.append(n % 2)
# #
# # print(lista_paritate)
#
# lista_pritate = [n % 2 for n in lista_nr if n % 3 == 0]
#
# dict_paritate = {n: n % 2 for n in lista_nr}
#
# print(dict_paritate)


# car = {'hyudai': 20000,
#     'BMW': 50000,
#     'Toyota': 30000,
#     'Mercedes': 100000,
#     'Dacia': 13000
# }
#
# # car_ron = {}
# #
# # for name, price in car.items():
# #     car_ron[name] = f'{price * 5} RON'
#
# car_ron = {name: f'{price * 5} RON' for name, price in car.items()}
# car_cheap = {name: price for name, price in car.items() if price < 40000}
#
# print(car_ron)
# print(car_cheap)

# car_names = [None for _, _ in car.items()]
# print(car_names)

# for _ in range(100):
#     print("Salut!")

# n = 5000000
# my_list = []
#
# for i in range(n):
#     my_list.append(i)
#
# current_time = time()
#
# # my_list2 = []
# # for i in my_list:
# #     if i % 2 == 0:
# #         my_list2.append(i * i)
# my_list2 = [i * i for i in my_list if i % 2 == 0]
#
# print(time() - current_time)

# numbers = [1, 1, 3, 7, 9, 2, 3, 100, 9, 333, 2.0, 5, 1, 3, 3]
# numbers_dict = {num: numbers.count(num) for num in numbers}
#
# print(numbers_dict)

# files = ['mare_2023.jpeg', 'test.txt', 'liste.py', 'cv.pdf', 'munte_2026.png']
#
# paths = {
#     'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
#     'C://Downloads//Text': ['txt'],
#     'C://Downloads//Python_files': ['py'],
#     'C://Downloads//PDF': ['pdf'],
# }
#
# file_paths = {}
# file_paths = {file: path for file in files for path, extensions in paths.items() if file.split('.')[-1] in extensions}

# for file in files:
#     extension = file.split('.')[-1]
#
#     for path, extensions in paths.items():
#         if extension in extensions:
#             file_paths[file] = path
#             break

# paths_rev = {}
# for path, extensions in paths.items():
#     for extension in extensions:
#         paths_rev[extension] = path
#
# print(paths_rev)
#
# for file in files:
#     extension = file.split('.')[-1]
#     file_paths[file] = paths_rev[extension]
#
# print(file_paths)

# pairs = []
#
# for i in range(10):
#     for j in range(10):
#         # pairs.append((i, j))
#         pairs.append(str(i) + str(j))
#
# print(pairs)

pairs = (str(i) + str(j) for i in range(10) for j in range(10))
for pair in pairs:
    print(pair)
print(pairs)