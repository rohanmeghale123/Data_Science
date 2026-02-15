# Write a program to calculate the percentage of student based on marks of any 5 subjects.
sub1=int(input("Enter marks:"))
sub2=int(input("Enter marks:"))
sub3=int(input("Enter marks:"))
sub4=int(input("Enter marks:"))
sub5=int(input("Enter marks:"))
summarks=sub1+sub2+sub3+sub4+sub5
percen=summarks/5

print(f"Total percentage of students ={percen}%")