class Complex:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def show1(self):
        print("show function 1")
        print(self.a)
        print(self.b)
    
        
    def show2(self):
        print("show function 2")
        print(self.a)
        print(self.b)
        

obj1 = Complex(10,20)
obj2 = Complex(30,40)
obj1.show1()
obj2.show2()