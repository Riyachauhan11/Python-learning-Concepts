# Grand Parent class
class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):
    # Parent class
    def __init__(self, make, model, fuel, air_conditioning, sunroof):

        super(Car, self).__init__(make, model, fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof


class Electric_vehicle(Car):
    # Child class
    def __init__(self, make, model, fuel, air_conditioning, sunroof, distance):

        super(Electric_vehicle, self).__init__(
            make, model, fuel, air_conditioning, sunroof)

        self.distance = distance


my_obj = Electric_vehicle('Tesla', 2019, 'electric', True, True, 500)
print(my_obj.__dict__)
