class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a=None,b=None,c=None):
        total = 0  
        if(a!=None and b!=None and c!=None):
            total = a + b + c
        elif a!=None and b!=None:
            total = a + b
        else:
            total = a
            
        return total
            
            
s1 = student(50,50)
print(s1.sum(5,9,7))