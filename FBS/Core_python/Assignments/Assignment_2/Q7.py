# Find the sum of three-digit number.
a=int(input('enter three digit number:'))
hund=a//100
ten=(a//10)%10
unit=a%10
sum=hund+ten+unit
print(f'sum of digits ={sum}')