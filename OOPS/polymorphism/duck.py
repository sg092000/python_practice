class VS_Code:
    def execute(self):
        print("compiling")
        print("running")
        
class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")
        
class Laptop:
    def code(self,ide):
        ide.execute()
        
        
#ide = MyEditor()
lap = Laptop()
lap.code(MyEditor())