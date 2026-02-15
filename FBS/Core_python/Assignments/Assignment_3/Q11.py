#Accept age of five people and also per person ticket amount and then calculate total 
#amount to ticket to travel for all of them based on following condition : 
#a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
#c. Others need to pay full. 

ticket_Amt=float(input('enter ticket amount:'))
amount=0
for i in range(1,6):
    age=int(input('enter age:'))
    if age<12:
        pay=ticket_Amt*(70/100)
        print(f"Person {i}: Child discount applied, Pay = {pay}")
    elif age>59:
        pay=ticket_Amt*.50
        print(f"Person {i}: senior discount applied, Pay = {pay}")
    else:
        pay=ticket_Amt
        print(f'Person {i}: no discount ,pay {pay}')
    
    amount+=pay
print('Total ticket amount =',amount)
