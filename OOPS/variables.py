class Car:
    wheels = 4
    def __init__(self):
        self.com = "BMW"
        self.model = 1
        
c1 = Car()
c2 = Car()

print(c1.com,c1.model,c1.wheels)
print(c2.com,c2.model,c2.wheels)
c1.com = "AUDI"
Car.wheels = 8

print(c1.com,c1.model,c1.wheels)
print(c2.com,c2.model,c2.wheels)