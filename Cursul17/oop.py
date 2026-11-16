class Produs:
    def __init__(self, nume: str, categorie: str, pret: float, reducere: float, stoc: int):
        self.nume = nume
        self.categorie = categorie
        self.pret = pret
        self.reducere = reducere
        self.stoc = stoc

    def pret_real(self):
        return self.pret * (1 - self.reducere)

    def display_info(self):
        return f"Produs(Nume: {self.nume}, Categorie: {self.categorie}, Pret real: {self.pret_real()}, Stoc: {self.stoc})"

class Magazin:
    def __init__(self, nume: str, adresa: str, capital: float = 0):
        self.nume = nume
        self.adresa = adresa
        self.capital = capital
        self.produse = []

    def achizitionare_produs(self, produs: Produs, pret: float= 0):
        if self.capital < pret:
            return False
        self.capital -= pret
        self.produse.append(produs)
        return True

    def vindere_produs(self, nume_produs: str, nr_bucati: int):
        for produs in self.produse:
            if produs.nume == nume_produs and produs.stoc >= nr_bucati:
                self.capital += produs.pret_real() * nr_bucati
                produs.stoc -= nr_bucati
                return True
        return False

    def display_info(self):
        ret_str: str = f"Capital: {self.capital}\nProduse:"
        for produs in self.produse:
            ret_str += f"\n{produs.display_info()}"
        return ret_str


if __name__ == "__main__":
    produse = [
        Produs("Laptop Asus VivoBook", "Electronice", 3500, 0.1, 5),
        Produs("Telefon Samsung Galaxy A54", "Telefoane", 1800, 0.15, 12),
        Produs("Căști Sony WH-1000XM5", "Audio", 1200, 0.2, 8),
        Produs("Monitor LG 27 inch", "Monitoare", 900, 0.05, 3),
        Produs("Tastatură Logitech MX Keys", "Periferice", 550, 0, 15),
        Produs("Mouse Razer DeathAdder", "Periferice", 350, 0.25, 20),
        Produs("Imprimantă HP LaserJet", "Imprimante", 750, 0.1, 6),
        Produs("Tabletă iPad Air", "Tablete", 2800, 0.05, 4),
        Produs("SSD Samsung 1TB", "Stocare", 450, 0.3, 25),
        Produs("Webcam Logitech C920", "Periferice", 400, 0.15, 9),
    ]

    magazin = Magazin("Flanco", "Bucuresti, Sector 6, Strada Dreptatii, Nr 15", capital=50000)
    for produs in produse:
        magazin.achizitionare_produs(produs, pret=produs.pret_real() * 0.5 * produs.stoc)


    print("Buna ziua!")

    while True:
        print(magazin.display_info())
        nume_produs = input("Ce produs doriti sa cumparati (stop pentru a va opri)? ")
        if nume_produs == "stop":
            print("O zi buna!")
            break
        nr_bucati = int(input("Cate bucati? "))
        vandut = magazin.vindere_produs(nume_produs, nr_bucati)
        if vandut:
            print("Multumim pentru achizitie!")
        else:
            print("Ne cerem scuze, produsul cu numele si numarul de bucati cerute nu exista in stoc!")