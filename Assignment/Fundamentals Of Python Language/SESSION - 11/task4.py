"""Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, 
use the keys(), values(), and items() methods to print: a) all food items, b) all quantities,
and c) each item with its quantity."""

food_order={'Pizza': 2, 'Burger': 1, 'Fries': 3}

print("a)  all food items: ")
for item in food_order.keys():
    print(item)


print("\nb) all quantities: ")
for quantities in food_order.values():
    print(quantities)

    
print("\nc) each item with its quantity : ")
for item, quantity in food_order.items():
    print(f"{item}:{quantity}")