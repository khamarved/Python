#Define a function called get_discounted_price that takes price and discount_percent as arguments and returns
# the final price after applying the discount.
 #Test it with a price of 500 and a discount of 10%.
def get_discounted_price(price, discount_percent):
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
price=int(input("Enter price"))
discount_percent=int(input("Enter discount percentage "))
result=get_discounted_price(price,discount_percent)
print (result)