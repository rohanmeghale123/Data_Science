gender=input('enter gender (F/M):')
age=int(input('enter age:'))
if gender in ['f',"F",'female','FEMALE']:
    if age>17:
        print('eligible for shadi')
    else:
        print("padhai kar le")

else:
    if age>21:
        print('eligible for marriage')
    else:
        print('not eligible')