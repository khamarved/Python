"""Using reduce() and a lambda function, calculate the total bill amount for a Swiggy order 
given a list of item prices: [120, 80, 150, 60]. <br><br><em><strong>Hint:</strong> Import reduce from functools.</em>"""

from functools import reduce
item_prices=[120,80,150,60]
total_bill = reduce(lambda x,y: x+y, item_prices)
print(total_bill)