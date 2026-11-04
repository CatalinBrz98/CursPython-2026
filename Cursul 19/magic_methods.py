class Vehicle:
    contor: int

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f'Vehicle: {self.brand}, {self.model}, {self.color}'
Vehicle.contor = 0

class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return celcius * 1.8 + 32

    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return fahrenheit - 32 * 1.8

if __name__ == '__main__':
    my_car = Vehicle('Toyota', 'Yaris', "Blue")
    # print(my_car, str(my_car), repr(my_car))
    # print(f'{my_car} {my_car.show_info()} {my_car.show_info()}')
    print({"my_car": my_car})

    a = 1
    b = 2
    print(a + b)
    print(a.__add__(b))