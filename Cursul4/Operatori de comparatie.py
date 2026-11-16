a = 10
# if a > 5:
#
#     if a < 20:
#         print("Conditie respectata")
#     else:
#         print("Conditie nerespectata")
#
# else:
#     print("Conditie nerespectata")

# if a > 5 and a < 20:
#     print("Conditie respectata")
# else:
#     print("Conditie nerespectata")

# if not(a > 5 and a < 20):
#     print("Conditie nerespectata")

# litera = "c"
# nume = "Catalin"
# text = "Salut, eu sunt Marius si il cunosc pe Catalin."
# if litera in nume:
#     print("Conditie respectata")
# else:
#     print("Conditie nerespectata")

# if True:
#     if True:
#         if True:
#             if True:
#                 print("Cazul 1")
#         else:
#             print("Conazul 2")

bmi = 26
# if 0 < bmi <= 18.5:
#     print("Underweight")
# if 18.5 < bmi <= 25:
#     print("Normal")
# if 25 < bmi <= 30:
#     print("Overweight")
# if 30 < bmi:
#     print("Obese")

# if bmi <= 18.5:
#     print("Underweight")
# else:
#     if bmi <= 25:
#         print("normal")
#     else:
#         if bmi <= 30:
#             print("Overweight")
#         else:
#             print("Obese")


# if bmi <= 18.5:
#     print("Underweight")
# elif bmi <= 25:
#     print("Normal")
# elif bmi <= 30:
#     print("Overweight")
# else:
#     print("Obese")



nume = "test"

match nume:
    case "Catalin":
        print(27)
    case "Viorel":
        print(23)
    case "Ioana" | "Viola":
        print(24)
    case _:
        print(100)