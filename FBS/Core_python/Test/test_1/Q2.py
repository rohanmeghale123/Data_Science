# write a program to calculate simple interest based on principal ,rate and time (SI=P*R*T/100)

p=float(input('enter principal amount:'))
r=float(input('enter rate:'))
t=int(input('enter time:'))
si=(p*r*t)/100
print(f'Simple interest ={si}')