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
        # parent attributes
        Vehicle.make = make
        Vehicle.__model = model
        Vehicle.__fuel = fuel

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.__model, " ", Vehicle.__fuel)

    def show_privatemethod_ofparent(self):
        self._Vehicle__private_method_parent()


obj1 = Car(2019, 'Tesla', 'electric', True, True)
print(obj1.__dict__)
obj1.show_parent_attribute()
print(obj1.make)
# print(obj1.__model,obj1.model) - both will throw an error
# print(obj1.__private_method_parent) will also throw error
obj1.show_privatemethod_ofparent()
obj1._Vehicle__private_method_parent()
