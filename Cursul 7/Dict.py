my_dict = {"prenume": "Catalin", "nume": "Breaz", "varsta": 27}

print(my_dict)

my_dict["prenume"] = "Mihai"
my_dict["sex"] = "male"

print(my_dict)

if "Catalin" in my_dict:
    print(my_dict["prenume"])
#
# persons = [{"prenume": "Catalin", "nume": "Breaz", "varsta": 27}]

# pers_varsta = {"Breaz Catalin": 27, "Mihai Mihailescu": 34, "George Ene": 19, "Andreea Grecu": 29}
# pers_varsta = {("Breaz", "Catalin"): 27, ("Mihai", "Mihaiescu"): 34, ("George", "Ene"): 19, ("Andreea", "Grecu"): 29}

# print(pers_varsta[("Breaz", "Catalin")])
# print(pers_varsta[("Andreea", "Grecu")])

# for cheie, valoare in pers_varsta.items():
#     print(f'Cheie: {cheie}, valoare: {valoare}')
