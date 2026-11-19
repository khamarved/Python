
class employee():
    def __init__(self,a,b):
        print("Initial Method")
        self.a=a
        self.b=b
    
    def __str__(self):
        return f"{self.a},{self.b}"
    
    def __add__(self, obj):
        x = self.a+obj.a
        y = self.b+obj.b
        return(x,y)
        
    def __sub__(self,obj):
            x = self.a-obj.a
            y = self.b-obj.b
            return(x,y)
        

    def __mul__(self,obj):
            x = self.a*obj.a
            y = self.b*obj.b
            return(x,y)
        

obj = employee(10,20)
print(obj)

obj1 = employee(50,60)
print(obj1)

print("Addition : ",obj+obj1)        

print("Substraction : ",obj-obj1)        

print("Multiplication : ",obj*obj1)        
        
        