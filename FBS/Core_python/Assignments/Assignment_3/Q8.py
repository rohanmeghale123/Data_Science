#Write a program to prompt user to enter userid and password. After verifying userid and password displaya 4 digit random 
# number and ask user to enter the same. If user enters the same number then show him success message otherwise failed.
#  (Something like captcha)

import random

# Predefined user id and password
correct_userid = "admin"
correct_password = "1234"

# Take input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Verify login
if userid == correct_userid and password == correct_password:
    print("Login successful ✅")

    # Generate 4-digit random number (captcha)
    captcha = random.randint(1000, 9999)
    print("Your captcha is:", captcha)

    # Ask user to enter captcha
    user_captcha = int(input("Enter the same 4-digit number: "))

    # Verify captcha
    if user_captcha == captcha:
        print("Verification successful 🎉")
    else:
        print("Verification failed ❌ Wrong number entered")

else:
    print("Invalid User ID or Password ❌")
