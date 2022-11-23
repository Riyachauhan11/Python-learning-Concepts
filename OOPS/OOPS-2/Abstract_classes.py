from abc import ABC, abstractmethod
# ABC - abstract class


class Vehicle(ABC):

    @abstractmethod
    def get_model(self):
        print(self.model)


class Car(Vehicle):

    def __init__(self, make, model, fare):
        self.make = make
        self.model = model
        self.fare = fare

    def get_model(self):
        super().get_model()


myobj = Car('Tesla', 2019, 40)
myobj.get_model()

# myobj1 = Vehicle() - throws an error
''' cause Vehicle() is a base abstract class and no implementation occurs there'''
