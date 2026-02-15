# WAP to calculate selling price of book based on cost price and discount.
cost_price=float(input("enter price of book:"))
discount=float(input("enter discount percentage:"))
dis_amt=(cost_price*discount)/100
selling_price=cost_price-dis_amt
print(f'selling price of the book ={selling_price}')