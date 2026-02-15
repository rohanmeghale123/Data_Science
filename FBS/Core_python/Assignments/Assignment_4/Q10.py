#
num=int(input('enter a number:'))
sum=0
for i in range(1,num):
    if num%i==0:
        print(i,end=' ')
        sum=sum+i
print(f'sum of number is {sum}')
if sum==num:
    print(f'{num} is a perfect number') 
else:
    print(f'{num} is not a perfect number')