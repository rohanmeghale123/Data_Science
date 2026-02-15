# Write a program to check if user has entered correct userid and password.
uid='admin1'
password='121212'
userid=input('enter user id:')
passwords=input('enter password:')

if(uid==userid and password==passwords):
    print('userid and password is right')
else:
    print('userid and password is wrong')
    