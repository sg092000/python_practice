class A:
    def fun1(self):
        print("1 function")
    def fun2(self):
        print("2 function")
        
        
class B(A):
    def fun3(self):
        print("3 function")
    def fun4(self):
        print("4 function")
        
        
b1 = B()
a1 = A()

b1.fun1()
b1.fun3()
a1.fun2()