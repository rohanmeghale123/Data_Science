# Convert distant given in feet and inches into meter and centimeter.
feet=int(input("enter distance in feet :"))
inch=int(input("enter distance in inches :"))
total_cm=(feet*30.48)+(inch*2.54)
meter=total_cm//100
centimetr=total_cm%100
print(f'meter ={meter},and centimeter = {centimetr}')
