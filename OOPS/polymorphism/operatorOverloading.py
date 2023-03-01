class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        sum1 = self.m1 + other.m1
        sum2 = self.m2 + other.m2 
        sum3 = Student(sum1,sum2)
        return sum3 
    
    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        return s1 > s2
    
s1 = Student(50,69)
s2 = Student(60,50)
s3 = s1 + s2
print(s3.m2) 


if(s1 > s2):
    print("s1 wins")
else:
    print("s2 wins")