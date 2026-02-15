# Write a program to calculate profit or loss. 
cp=float(input('enter cost price:'))
sp=float(input('enter selling price:'))
if sp>cp:
    profit=sp-cp
    print(f'Profit {profit}')
else:
    loss=cp-sp
    print(f'Loss {loss}')
