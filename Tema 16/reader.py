import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def write_csv(file_name, columns, data):
    with open(file_name, "w", newline="") as g:
        writer = csv.DictWriter(g, columns)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    write_csv("tema.csv", ["id", "nume", "prenume"], data=[
        {"id": 1, "nume": "Breaz", "prenume": "Catalin"},
        {"id": 2, "nume": "Ionache", "prenume": "Mihai"},
        {"id": 3, "nume": "Terente", "prenume": "Luca"}
    ])
    read_csv("tema.csv")
