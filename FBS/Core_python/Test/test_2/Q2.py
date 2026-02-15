num=int(input('enter the 3 digit number:'))
a=num//100
b=(num//10)%10
c=num%10
print(a,b,c)
if (a*0.5==b) and (a==c*0.5):
    print("yes you have done it")
else:
    print("Please try next time")
