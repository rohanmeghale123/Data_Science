#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate 
# percentage. Display all percentage and average percentage of students. 

num=int(input('enter the number of students:'))
finalall=0
for i in range(1,num+1):
    print(f'student{i}')
    sum=0
    for j in range(1,6):
         marks=int(input(f'enter the marks of student sub {j}:'))
         sum=sum+marks
    per=sum/5
    print(f'percentage of student {i} is {per}')
    finalall+=per
finalper=finalall/num
print(f'final percentage of all students is {finalper}')    
