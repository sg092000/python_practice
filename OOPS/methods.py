class Student:
    school = "Christ School"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("this is a static method of class school")
        a = 50
        return a
        
        
        
s1 = Student(30,40,50)
s2 = Student(60,70,80)

print(s1.get_m1())
s1.set_m1(50)
print(s1.get_m1())

print(Student.getSchool())

print(Student.info())
