# WAP to check if a given number is prime number or not. 
a=int(input('enter a number:'))

if a%2==0 or a%3==0:
    print("given number is not prime")
else:
    print("given number is prime")