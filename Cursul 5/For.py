# text = "Hello131 W%orld!"
#
# for char in text:
#     if char.isdigit():
#         print(f"{char} is digit")
#     elif char.isalpha():
#         print(f"{char} is alpha")
#     else:
#         print(f"{char} is something else")

# numar = input()
#
# prod = 1
#
# for cifra in numar:
#     prod *= int(cifra)
#
# print(prod)

# for i in range(0, 10000, 300):
#     print(i)


# text = "We learn Python!"
# text2 = "Avem un text de "
#
# for i, char in enumerate(text):
#     print(char, text2[i])

# exista_divizor = False
#
# for i in range(600, 700):
#     print(i)
#     if i % 123 == 0:
#         exista_divizor = True
#         break
#
# if exista_divizor:
#     print("Exista divizor")
# else:
#     print("Nu exista divizor")

# for i in range(10):
#     if i % 3 != 0:
#         continue
#
#     print(i)

# numar = int(input())
# suma = 0
# while numar > 0:
#     cifra = numar % 10
#     numar //= 10
#
# print(suma)

nume = ["Ana", "Maria", "Catalin", "Andrei", "Cosmin", "Mihaela"]
varsta = [20, 54, 27, 32, 39, 29]
sex = ["F", "F", "M", "M", "M", "F"]
este_angajat = [True, False, True, False, False, True]

angajati_barbati_peste_30 = 0
somere_femei = 0

for i, n in enumerate(nume):
    if sex[i] == "M" and este_angajat[i] and varsta[i] > 30:
        angajati_barbati_peste_30 += 1
    if sex[i] == "F" and not este_angajat[i]:
        somere_femei += 1
    # print(f"Nume: {n}, varsta: {varsta[i]}, sex: {sex[i]}, este_angajat: {este_angajat[i]}")

print(f"Exista {angajati_barbati_peste_30} barbati angajati peste 30 de ani")
print(f"Exista {somere_femei} femei somere")
