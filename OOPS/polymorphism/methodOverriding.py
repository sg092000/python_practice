class parent:
    def show(self):
        print("parent is here")
        
class child(parent):
    #pass
    def show(self):
        print("child is here")
        
obj = child()
obj.show()