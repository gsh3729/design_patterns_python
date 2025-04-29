class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.wheels = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.color} color and {self.wheels} wheels."


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine
        return self  # fluent interface

    def set_color(self, color):
        self.car.color = color
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def build(self):
        return self.car

builder = CarBuilder()
car = builder.set_engine("V6").set_color("Black").set_wheels(4).build()
print(car)