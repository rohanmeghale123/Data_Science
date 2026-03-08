#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to 
# re-enter the credentials. Let him try 3  times. After that program to terminate. 

uid=1234
passw="abcd"
for i in range(3):
    u_id=int(input("Enter your u_id: "))
    password=input("Enter your password: ")
    if u_id==uid and password==passw:
        print("correct password")
        break
    else:
        print("re enter the password")
    