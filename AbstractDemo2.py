from abc import ABC,abstractmethod

class Base(ABC):
    @abstractmethod
    def Addition(self,no1,no2):
        pass

class Derived(Base):
    def Addition(self,no1,no2):
        return no1+no2

dobj=Derived()             
ret=dobj.Addition(10,11)

print("Addition is:",ret)
