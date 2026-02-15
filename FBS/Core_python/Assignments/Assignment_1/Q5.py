# Write a program to enter P, T, R and calculate Compound Interest.
# Write a program to enter P, T, R and calculate simple Interest.
p=float(input("Enter Principal amount:"))
r=float(input("Enter Rate:"))
t=float(input("enter no. fo years:"))
amt=p*((1+r/100)**t)
ci=amt-p
print(f'Compound Interest = {ci}')
print(f"Total Amount = {amt}")