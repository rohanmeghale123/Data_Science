#Take input
num1=int(input('Enter number 1:'))
num2=int(input('Enter number 2:'))

#Perform addition
sum=num1+num2

#Display result
#print("Addition is",sum)              #okk
print('Addition is '+str(sum))         #okk
#print('addition is'str(sum))           #wrong

print(f'Addition is {sum}.')
print(f'Addition of {num1} and {num2} is {sum}.')
