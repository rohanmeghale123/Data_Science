# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 
gender=input('enter gender:')
age=int(input('enter age:'))
if gender in ['F','f','FEMALE','female']:
    if age>=18:
        print('eligible to marry')
    else:
        print('not eligible to marry')
else:
    if age>=21:
        print('eligible to marry')
    else:
        print('not eligible to marry')
