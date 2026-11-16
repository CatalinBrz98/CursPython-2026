import csv

def read_from_db(file_path):
    db_data = []

    with open(file_path, "r") as f:
        db_reader = csv.DictReader(f)
        for row in db_reader:
            db_data.append(row)

    return db_data