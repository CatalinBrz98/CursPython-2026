# from copy import deepcopy

# lista = [1, 2, 3, 1.24, "String"]
# print(lista)
# print(type(lista))


# a = 1
# b = 2
# c = [1, 2, 3]
# lista_my_var = [a, b, c, b, c]
# print(lista_my_var)
# print(len(lista_my_var))
# c += [4]
# b += 1
# print(lista_my_var)
# print(len(lista_my_var))

# a = [1, 2]
# b = [1, 2]
# c = a
#
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))
#
# a += [3, 4]
#
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# print(lista1, id(lista1))
# print(lista2, id(lista2))
# lista2 = (lista1 + lista2)
# print(lista1, id(lista1))
# print(lista2, id(lista2))
# lista2 += lista1
# print(lista1, id(lista1))
# print(lista2, id(lista2))

# lista_mea = [1, 2, 3]
# print(lista_mea, id(lista_mea))
# # lista_mea = lista_mea * 3
# lista_mea *= 3
# print(lista_mea, id(lista_mea))

# list1 = [1, 2.56, "Test", [1, 2, 3, 4], 6, 1, 1]
# list1 = [6, 2, 3262, 43, 3 ,1 ,1]
# list1 = [[1, 2, 3], [15, 16, 17], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
# print(dir(list1))
# list1.append(5)
# list2 = list1.copy()
# list2 = deepcopy(list1)
# list2.append(5)
# list2[3].append(100)
# list1.extend([1, 2, 3, 4])
# print(list1)
# if 151 in list1:
#     print(list1.index(151))
# list1.insert(2, 3000)
# print(list1)
# print(list1.pop())
# print(list1.count(152362))
# if 151 in list1:
#    list1.remove(151)
# list1.reverse()
# list1.sort()
# print(list1)
#
# if type(o) is str:

# print(list2)


my_word_list = "Uite o propozitie pe care o am".split()
print(my_word_list)
my_sentence = " ".join(my_word_list)
print(my_sentence)