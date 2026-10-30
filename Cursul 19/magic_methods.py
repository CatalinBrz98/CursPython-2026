class Vehicle:
    contor: int

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f'Vehicle: {self.brand}, {self.model}, {self.color}'
Vehicle.contor = 0


if __name__ == '__main__':
    my_car = Vehicle('Toyota', 'Yaris', "Blue")
    # print(my_car, str(my_car), repr(my_car))
    # print(f'{my_car} {my_car.show_info()} {my_car.show_info()}')
    print({"my_car": my_car})

    a = 1
    b = 2
    print(a + b)
    print(a.__add__(b))