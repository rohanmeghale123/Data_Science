#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a=int(input('enter triangle first:'))
b=int(input('enter triangle second: '))
c=int(input('enter triangle third: '))
sum=a+b+c
if(sum==180):
  if(a==b and b==c):
     print('Triangle is equilateral')
  elif (a==b or b==c or a==c):
    print('Triangle is isosceles')
  elif (a!=b and b!=c and a!=c):
    print('Triangle is scalene')
else:
  print('This is not triangle.')