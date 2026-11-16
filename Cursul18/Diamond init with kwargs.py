class ClasaA:
    def __init__(self, a, *args, **kwargs):
        self.a = a
        print("Init A")

    def vorbeste(self):
        print(self.a)
        print("Vorbeste A")

class ClasaB(ClasaA):
    def __init__(self, b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b = b
        print("Init B")

    def vorbeste(self):
        print(self.a, self.b)
        print("Vorbeste B")

class ClasaC(ClasaA):
    def __init__(self, c, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c
        print("Init C")

    def vorbeste(self):
        print(self.a, self.c)
        print("Vorbeste C")

class ClasaD(ClasaB, ClasaC):
    def __init__(self, d, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.d = d
        print("Init D")

    def vorbeste(self):
        print(self.a, self.b, self.c, self.d)
        print("Vorbeste D")

if __name__ == "__main__":
    a = ClasaA(a=1)
    b = ClasaB(a=1, b=2)
    c = ClasaC(a=1, c=3)
    d = ClasaD(a=1, b=2, c=3, d=4)

    a.vorbeste()
    b.vorbeste()
    c.vorbeste()
    d.vorbeste()

    print(ClasaD.mro())
