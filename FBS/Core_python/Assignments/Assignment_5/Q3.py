#Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total 
# amount to ticket to travel for all of them based on following condition :  
#a. Children below 12 = 30% discount  
#b. Senior citizen (above 59) = 50% discount  
#c. Others need to pay full.  

passs=int(input("enter the no.of passengers:"))
perti=100
sum=0
for i in range(1,passs+1):
    age=int(input("enter the age of passenger:"))
    if age<=12:
        print("child ticket")
        child=perti*.30
        sum=sum+child
    elif age>=59:
        print("senior citizen ticket")
        senior=perti*.50
        sum=sum+senior
    else:
        print("pay full ticket")
        sum=sum+perti

print(f"total amount to be paid is {sum}")