def sum(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

sum(2,3,4)


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs["model"]
        self.make = kwargs["make"]

camry = Car(model="Camry", make = "Toyota")
print(camry.make)
print(camry.model)
