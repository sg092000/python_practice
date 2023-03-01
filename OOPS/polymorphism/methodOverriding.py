class parent:
    def show(self):
        print("parent is here")
        
class child(parent):
    pass
        
obj = child()
obj.show()