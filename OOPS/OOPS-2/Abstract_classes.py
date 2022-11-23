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


##########################################################################


from abc import ABC, abstractmethod


class TextReaderAbstract(ABC):

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    @abstractmethod  # this is just an interface or "RULE"
    def get_path(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass


class TextReader(TextReaderAbstract):

    def get_path(self):
        return self.path

    def get_filename(self):
        return self.filename


myobj = TextReader("/users/download", 'SAMPLE.txt')
print(myobj.get_filename())
print(myobj.get_path())
