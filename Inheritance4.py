class Base():
    def fun(self):
        print("Inside base fun")


class Derived(Base):    
    def __init__(self):
        super().__init__()                          #To call parent
        print("Inside Derived Constructor")

dojb=Derived()
dojb.fun()