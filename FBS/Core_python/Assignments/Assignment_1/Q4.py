# Write a program to enter P, T, R and calculate simple Interest.
p=float(input("Enter Principal amount:"))
r=float(input("Enter Rate:"))
t=float(input("enter no. fo years:"))
si=(p*r*t)/100
print(f'Simple Interest = {si}')