# WAP to print all integers upto n that aren’t divisible by 2 and 3. 
num=int(input("enter a number:"))
i=0
while i<=num:
    if i%2!=0 and i%3!=0:
        print(i)
    i=i+1
