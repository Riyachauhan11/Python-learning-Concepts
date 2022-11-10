# Parent class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        # private
        self.__model = model
        self.__fuel = fuel

    def __private_method_parent(self):
        print("This is Private")


class Car(Vehicle):
    # Child class
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car, self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof


obj1 = Car(2019, 'Tesla', 'electric', True, True)
print(obj1.__dict__)
obj1._Vehicle__private_method_parent()
print(obj1.make)
