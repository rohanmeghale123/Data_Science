# Write a program to calculate area of an equilateral triangle.
base=int(input("enter base:"))
height=int(input("enter height:"))
area=base*height
equarea=((3**0.5)/4)*(area**2)
print(f'Equilateral triangle = {equarea}')

