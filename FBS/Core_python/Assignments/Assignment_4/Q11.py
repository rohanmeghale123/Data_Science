#
num=int(input('enter a number:'))
temp=num
while temp>0:
    temp=temp%10
    print(temp)
    temp=temp//10
