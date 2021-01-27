def is_leap(year):
    
    leap = False

    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap
    # y = int(year)
    # return y % 400 == 0 and (y%100 != 0 or y%4 == 0); 
year = int(input())
print(is_leap(year))