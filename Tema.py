import csv

def make_raport(clienti_file_name, comenzi_file_name, raport_file_name):
    with open(clienti_file_name, "r") as clienti_file, open(comenzi_file_name, "r") as comenzi_file:
        clienti_reader = csv.DictReader(clienti_file)
        clienti_dict = {}
        for client in clienti_reader:
            clienti_dict[client["id_client"]] = client["nume_client"]

        comenzi = []
        comenzi_reader = csv.DictReader(comenzi_file)
        for comanda in comenzi_reader:
            id_client = comanda["id_client"]
            nume_client = clienti_dict[id_client]
            comanda["nume_client"] = nume_client
            del comanda["id_client"]
            comenzi.append(comanda)

    with open(raport_file_name, "w", newline="") as raport_file:
        raport_keys = ["id_comanda", "nume_client", "suma", "data"]
        raport_writer = csv.DictWriter(raport_file, fieldnames=raport_keys)
        raport_writer.writeheader()

        for comanda in comenzi:
            raport_writer.writerow(comanda)


if __name__ == "__main__":
    make_raport("clienti.csv", "comenzi.csv", "raport.csv")