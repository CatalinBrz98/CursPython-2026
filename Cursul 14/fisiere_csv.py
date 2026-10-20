import csv


def read_csv(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row[2])

def write_csv(output_file):
    with open(output_file, "a", newline="") as g:
        writer = csv.writer(g)
        writer.writerow(["Mihai", "Cretu", "mihaita", "pass1234", "mihaita@gmail.com"])

def write_math(output_file):
    with open(output_file, "w", newline="") as g:
        writer = csv.writer(g)
        lines = [[i, i * 5, i * i] for i in range(10)]
        writer.writerows(lines)

def write_csv_dict(output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as g:
        field_names = ["nume", "categorie", "pret", "reducere", "stoc"]
        writer = csv.DictWriter(g, fieldnames=field_names)
        writer.writeheader()

        produse = [
            {"nume": "Laptop Asus VivoBook", "categorie": "Electronice", "pret": 3500, "reducere": 10, "stoc": 5},
            {"nume": "Telefon Samsung Galaxy A54", "categorie": "Telefoane", "pret": 1800, "reducere": 15, "stoc": 12},
            {"nume": "Căști Sony WH-1000XM5", "categorie": "Audio", "pret": 1200, "reducere": 20, "stoc": 8},
            {"nume": "Monitor LG 27 inch", "categorie": "Monitoare", "pret": 900, "reducere": 5, "stoc": 3},
            {"nume": "Tastatură Logitech MX Keys", "categorie": "Periferice", "pret": 550, "reducere": 0, "stoc": 15},
            {"nume": "Mouse Razer DeathAdder", "categorie": "Periferice", "pret": 350, "reducere": 25, "stoc": 20},
            {"nume": "Imprimantă HP LaserJet", "categorie": "Imprimante", "pret": 750, "reducere": 10, "stoc": 6},
            {"nume": "Tabletă iPad Air", "categorie": "Tablete", "pret": 2800, "reducere": 5, "stoc": 4},
            {"nume": "SSD Samsung 1TB", "categorie": "Stocare", "pret": 450, "reducere": 30, "stoc": 25},
            {"nume": "Webcam Logitech C920", "categorie": "Periferice", "pret": 400, "reducere": 15, "stoc": 9},
        ]

        writer.writerows(produse)

def read_csv_dict(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['username'])


if __name__ == '__main__':
    # read_csv("users.csv")
    # write_csv("users.csv")
    # write_math("math.csv")
    # write_csv_dict("produse.csv")
    read_csv_dict("users.csv")
