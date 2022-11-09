# Parent class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):
    # Child class
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        # parent attributes
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.model, " ", Vehicle.fuel)


obj1 = Car(2019, 'Tesla', 'electric', True, True)
print(obj1.__dict__)
print(obj1.show_parent_attribute())
print(obj1.make)
