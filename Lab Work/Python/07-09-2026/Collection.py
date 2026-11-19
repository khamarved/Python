#Collection
"""
List : is a Collection data type but we can store multiple types of data in single variable

denoted by []

mutable - changes

duplicate allows

orderable

"""
L = [10,10,60,20,True, "hello", "World", 1,1]
print(type(L))

L.append(100)
print(L)
print(L.count(1))
L.extend([6000,800,1000]) 
print(L)
L.pop(2)
print(L)
L.remove(1)
print(L)
