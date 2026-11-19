
from abc import ABC
class Employer(ABC):
    def salary(self):
        pass
class ved(Employer):
    def salary(self):
        return 500000

class kashish(Employer):
    def salary(self):
        return 100000
    
class Om(Employer):
    def salary(self):
        return 50000
    
obj = ved()
print(obj.salary())

obj = kashish()
print(obj.salary())

obj = Om()
print(obj.salary())

       