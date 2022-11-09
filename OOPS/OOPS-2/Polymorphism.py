1+2
"a"+"b"
len([1, 2, 3, 4])
len("my name is lavi")

''' same concatenation func used for int and str
    same len method used for int and str : polymorphism'''


# Parent class
class Vehicle():

    # class attributes
    current_year = 2021
    base_price = 1000

    def __init__(self, make, model, fuel):
        self.make = make
        # private
        self.__model = model
        self.__fuel = fuel

    def __private_method_parent(self):
        print("This is Private")

    # default function to get value of car
    def get_value(self):
        Vehicle.base_price = 1000
        age = Vehicle.current_year-self._Vehicle__model
        print("This is default method of parent")
        return Vehicle.base_price*(1/age)


class Car(Vehicle):
    # Child class
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car, self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    # Overriding method - replaces the parent default method
    def get_value(self):
        Vehicle.base_price = 5000
        age = Vehicle.current_year-self._Vehicle__model
        print("this is child override method")
        return Vehicle.base_price*(1/age)


obj1 = Car('Tesla', 2019, 'electric', True, True)
print(obj1.get_value())

parent_obj = Vehicle('Ford', 2018, 'petrol')
print(parent_obj.get_value())
