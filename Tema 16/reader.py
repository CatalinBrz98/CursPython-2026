import csv

def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv("tema.csv")
