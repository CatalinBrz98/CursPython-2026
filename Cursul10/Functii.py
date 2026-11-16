# # my_result = sum([1, 20])
# my_result = print("Salut!")
# print(my_result)
# my_lsit = [1, 2, 3]
# print(my_lsit.copy())
import sys


def name_and_age(name, age="-"):
    """
        Shows the name and age of the person
    :param name: a string with the name of the person
    :param age: an integer with the age of the person
    """
    return f"{name} is {age} years old."

def sum_and_diff(a, b):
    my_sum = a + b
    my_diff = a - b
    return my_sum, my_diff

# result_sum, result_diff = sum_and_diff(50, 34)
# print(result_sum)

def suma_numere(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

# suma_nr = suma_numere(1, 2, 3, 4, 5, 6, 7, 8)
# print(suma_nr)

def person_details(**kwargs):
    print(kwargs)
    if "name" in kwargs:
        print(f"The name of the person is {kwargs['name']}")

# person_details(name="Ana", age=29, surname="Smith")

another_var = 200

def my_function():
    another_var = 100
    print(another_var)

my_function()
print(another_var)