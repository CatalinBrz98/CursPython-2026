import sys


class Produs:
    def __init__(self, nume: str, categorie: str, pret: float, reducere: float, stoc: int):
        self.nume = nume
        self.categorie = categorie
        self.pret = pret
        self.reducere = reducere
        self.stoc = stoc

    @property
    def pret_real(self):
        return self.pret * (1 - self.reducere)

    @property
    def display_info(self):
        return f"Produs(Nume: {self.nume}, Categorie: {self.categorie}, Pret real: {self.pret_real}, Stoc: {self.stoc})"

class Magazin:
    def __init__(self, nume: str, adresa: str, capital: float = 0):
        self.__nume = nume
        self.__adresa = adresa
        self.__capital = capital
        self.__produse = []

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume: str):
        if isinstance(nume, str) and nume.isalpha():
            self.__nume = nume
        else:
            raise TypeError

    def achizitionare_produs(self, produs: Produs, pret: float= 0):
        if self.__capital < pret:
            return False
        self.__capital -= pret
        self.__produse.append(produs)
        return True

    def vindere_produs(self, nume_produs: str, nr_bucati: int):
        for produs in self.__produse:
            if produs.nume == nume_produs and produs.stoc >= nr_bucati:
                self.__capital += produs.pret_real * nr_bucati
                produs.stoc -= nr_bucati
                return True
        return False

    @property
    def display_info(self):
        ret_str: str = f"Capital: {self.__capital}\nProduse:"
        for produs in self.__produse:
            ret_str += f"\n{produs.display_info}"
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
        magazin.achizitionare_produs(produs, pret=produs.pret_real * 0.5 * produs.stoc)

    print(produse[0].pret_real)

    nume_magazin = magazin.nume
    print(nume_magazin, magazin._Magazin__nume)
    nume_magazin = "Hullaballoo"
    print(nume_magazin, magazin._Magazin__nume)

    magazin.nume = "Test"
    print(nume_magazin, magazin._Magazin__nume)

    print(sys.getsizeof(magazin))
