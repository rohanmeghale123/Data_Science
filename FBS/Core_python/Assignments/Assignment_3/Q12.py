# Write a program to check if given 3 digit number is a palindrome or not.
a=int(input('enter three digit:'))
a1=(a//100)
print(a1)
a2=(a//10)%10
print(a2)
a3=a%10
print(a3)
digit=(a3*100)+(a2*10)+a1
print(digit)
if digit==a:
    print('the 3 diit number is palindrome')
else:
    print('the 3 diit number is not palindrome')