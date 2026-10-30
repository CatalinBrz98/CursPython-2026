class Animal:
    def make_sound(self):
        print("Making sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo moo")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow(), Animal(), Cat()]
    for animal in animals:
        animal.make_sound()