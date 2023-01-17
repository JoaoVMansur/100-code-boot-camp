
#*Args
def add(*args):
    
    sum = 0
    for n in args:
        sum += n

    return sum


print(add(1, 2, 3, 4))

#**Kwargs

def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs.item():
    #     print(key)
    #     print(value)

    
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)
calculate(2, add=3, multiply=5)

#Create a class with lots of optional kwargs 

class Car():

    def __init__(self, **kw):

        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.ger("seats")

        

my_car = Car()