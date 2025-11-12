# check if a year is a leap year

year = int(input("Enter the year: "))

def leapyearOrNot(year: int) -> bool:
    check = False
    if (year % 4 == 0):
        if (year % 100 != 0):
            check = True
        elif( year % 400 == 0):
            check = True
    return check

if(leapyearOrNot(year)):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year ")

