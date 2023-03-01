class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name,self.age)
        
    class School:
        
        def __init__(self,school):
            self.school = school
        
        def show(self):
            print(self.school)
            
            
s1 = Student("sam",22)
s1.show()

sch1 = Student.School("christ")
sch1.show()