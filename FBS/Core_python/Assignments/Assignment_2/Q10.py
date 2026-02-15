# Write a program to reverse three-digit number.
a=int(input('enter three digit number:'))
hund=a//100
ten=(a//10)%10
unit=a%10
sum=(unit*100)+hund+(ten*10)
print(f'reverse three digits ={sum}')