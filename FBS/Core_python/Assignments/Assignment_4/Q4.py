# WAP to print factorial of a number .
n=int(input('enter number:'))
i=1
fact=1
while i<=n:
    fact*=i
    i=i+1
print(fact)