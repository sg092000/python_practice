class Complex:
    
    def __init__(self):
        self.name = "Sammy"
        self.age = 22
    def compare(self,other):
        return (self.age == other.age)

obj1 = Complex()
obj2 = Complex()

print(obj1.name)
print(obj2.name)

obj1.age = 30

if(obj1.compare(obj2)):
    print("same")
else : 
    print("different")