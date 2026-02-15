#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
basicsal=float(input("Enter the basic salary ="))
da=basicsal*0.1
ta=basicsal*.12
hra=basicsal*.15
total_Sal=basicsal+da+ta+hra
print(f'Total salary ={total_Sal}')
