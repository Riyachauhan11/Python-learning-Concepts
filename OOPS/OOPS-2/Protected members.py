# Parent class
class Vehicle():

    # class attributes
    current_year = 2021
    base_price = 1000

    def __init__(self, make, model, fuel):
        self.make = make

        # protected attributes
        self._model = model
        self._fuel = fuel

    # default function to get value of car
    def _get_value(self):
        age = Vehicle.current_year-self._model
        print("This is default method of parent")
        return Vehicle.base_price*(1/age)


class Car(Vehicle):
    # Child class
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car, self).__init__(make, model, fuel)

        # protected attributes
        self._air_conditioning = air_conditioning
        self._sunroof = sunroof

    # Overriding method - replaces the parent default method
    # protected method
    def _get_value(self):
        Vehicle.base_price = 5000
        age = Vehicle.current_year-self._model
        print("this is child override method")
        return Vehicle.base_price*(1/age)


myobj = Car('Tesla', 2019, 'electric', True, True)
print(myobj._air_conditioning)
print(myobj._sunroof)
print(myobj._get_value())
# print(myobj.fuel) or any protected attribute written without _ will throw an error
