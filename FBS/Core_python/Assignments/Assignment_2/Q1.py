# Convert the time entered in hh,min and sec into seconds.
hr=int(input("enter the hours:"))
min=int(input("enter the minute:"))
sec=int(input("enter the seconds:"))
total_sec=(hr*60*60)+(min*60)+sec
print(f"total seconds= {total_sec}")