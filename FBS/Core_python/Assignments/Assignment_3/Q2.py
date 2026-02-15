# Write a program to input any alphabet and check whether it is vowel or consonant.
a1=input('enter alphabet:')
if a1 in ['a','i','o','u','e','A','I','O','U','E']:
    print(f'{a1} is vowel')
elif a1 in ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
    print(f'{a1} is consonant')
else:
    print('entered value is wrong')