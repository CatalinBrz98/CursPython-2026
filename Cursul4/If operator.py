# nr = 12512

# paritate = None
# if nr % 2 == 0:
#     paritate = "par"
# else:
#     paritate = "impar"

# paritate = "par" if nr % 2 == 0 else "impar"
#
# print(nr, paritate)
#
# print(2 * (10 ** 3))

numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numere_parsate = [("par", num) if num % 2 == 0 else ("impar", num) for num in numere if num % 3 != 0]
print(numere_parsate)