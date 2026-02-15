# Write a program to input all sides of a triangle and check whether triangle is valid or not.
a1=int(input('enter triangle first:'))
a2=int(input('enter triangle second: '))
a3=int(input('enter triangle third: '))
if (a1+a2>a3) and (a1+a3>a2) and (a2+a3>a1):
    print('Triangle is valid')
else:
    print('Triangle is not valid')