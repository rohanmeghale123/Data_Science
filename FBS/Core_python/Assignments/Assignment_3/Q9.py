# Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

sub1=float(input('enter marks sub1:'))
sub2=float(input('enter marks sub2:'))
sub3=float(input('enter marks sub3:'))
sub4=float(input('enter marks sub4:'))
sub5=float(input('enter marks sub5:'))
per=((sub1+sub2+sub3+sub4+sub5)/5)

if per>=90:
    print('First class')
elif per>=70:
    print('Second class')
elif per>=35:
    print('Third class')
else:
    print("Fail")
    