i=0
sum=0
while i<5:
    p1=input('enter product name')
    pp=float(input('enter a price:'))
    print(p1)
    print(pp)
    sum+=pp
    i+=1
print(sum)
gst=sum*.18
print(gst)
total=gst+sum
print('Total value gst :',total)
