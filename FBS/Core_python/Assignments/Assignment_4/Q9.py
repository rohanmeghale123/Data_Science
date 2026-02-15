# WAP to print all numbers in a range divisible by a given number. 
num=int(input('enter a number:'))
for i in range(1,100):
    if i%num==0:
        print(i)
