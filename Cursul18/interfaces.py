class Printable:
    def print_func(self):
        raise NotImplementedError

class Scannable:
    def scan_func(self):
        raise NotImplementedError

class OldPrinter(Printable):
    def print_func(self):
        print("I printed something")

class ModernPrinter(Printable, Scannable):
    def print_func(self):
        print("I printed something")

    def scan_func(self):
        print("I scanned something")