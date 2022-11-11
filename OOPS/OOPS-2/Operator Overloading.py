class Vehicle():
    def __init__(self, make, model, fare):
        self.make = make
        self.model = model
        self.fare = fare

    def __str__(self):
        return "the make of the car is {} and the model is of {} with a fare of {}".format(
            self.make,
            self.model,
            self.fare)

    def __add__(self, other):
        return self.fare+other.fare

    def __sub__(self, other):
        return self.fare-other.fare


myobj = Vehicle('Tesla', 2019, 40)
myobj2 = Vehicle('Ford', 2018, 80)

print(myobj+myobj2)
print(myobj-myobj2)
