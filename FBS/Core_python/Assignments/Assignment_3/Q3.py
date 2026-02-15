# Write a program to input angles of a triangle and check whether triangle is valid or not
a1=int(input('enter triangle first:'))
a2=int(input('enter triangle second: '))
a3=int(input('enter triangle third: '))
sum=a1+a2+a3
if(sum==180):
    print('Triangle is valid')
else:
    print('Triangle is not valid')