class Car():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is", self.make, "from Car class"


class Electric_car():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is", self.make, "from Electric Car class"


class Taxi(Car, Electric_car):  # multiple inheritance
    def __init__(self, make, model, fuel):
        super().__init__(make, model, fuel)


myobj = Taxi('Tesla', 2019, 'electric')
print(myobj.get_car_details())

print(Taxi.__mro__)  # execution order
print(Taxi.mro())
