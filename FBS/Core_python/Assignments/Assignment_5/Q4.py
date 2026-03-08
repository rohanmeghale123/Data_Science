# WAP to print Armstrong number within a given range
val=0
n=int(input('enter the number of range:'))
for i in range(1,n+1):
    while i>0:
       d=i%10
       val+=d**3
       i//=10
    if val==i:
        print(i)
        print("okkk")
    val=0
    

