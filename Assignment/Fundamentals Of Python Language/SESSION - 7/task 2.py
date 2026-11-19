"""
Create a loop that goes through the following list:
['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King'], and breaks the
loop when it finds 'Burger King', printing 'Found Burger King, stopping search.'"""

food = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for item in food:
    if item == 'Burger King':
        print('Found Burger King, stopping search.')
        break
    print(item)