# Write a program to convert days into years, weeks and days.
days=int(input("enter number of Days:"))
years=days//365
remday=days%365
weeks=remday//7
computedays=remday%7
print(f"Years ={years},week ={weeks},days ={computedays}")