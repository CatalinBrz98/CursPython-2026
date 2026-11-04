class Printable:
    def printable(self):
        raise NotImplementedError

class Scannable:
    def scannable(self):
        raise NotImplementedError

class OldPrinter(Printable):
    def printable(self):
        print("I printed something")

class ModernPrinter(Printable, Scannable):
    def printable(self):
        print("I printed something")

    def scannable(self):
        print("I scanned something")