# N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent) 
n=int(input('enter the number of range:'))
s=0 
for i in range(1,n+1):
    s=s+(n**i)
print(s)
