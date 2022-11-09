class Circle(object):  # same as class Circle()
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "This is a circle which takes radius as an arguement"


c = Circle(30)
print(c)

'''object class has __init__, __str__, __new__ = 3 methods in object (default class)
   2 of which are being overriden above'''
