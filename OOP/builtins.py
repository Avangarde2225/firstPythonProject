class Kettle(object):

    power_source = "Electiricty"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True



kenwood = Kettle("Kenvood", 9.99)
print(kenwood.price)
print(kenwood.make)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.99)
print(hamilton.price)
print(hamilton.make)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

