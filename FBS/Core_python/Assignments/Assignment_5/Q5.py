#5. Write a program to print prime numbers between 1 to 100.
n=int(input('enter the number of range:'))
for i in range(1,n+1):  
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
