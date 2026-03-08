#a) 1! + 2! + 3! + 4! + .....n! 
n=int(input('enter the number of range:'))
s=0 
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+f   
print(s)
