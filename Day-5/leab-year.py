'''
Docstring for Day-5.leab-year
In the Gregon calender, three conditions are use to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be ecenly divided by 400, Then it is a leap year 
The year is also evenly dividible by 100 then it is not a leap year 
This mean that in the Gregorian calender the year 2000 and 2400 are leap year 
1900 2100 2200 2300 and 2500 are not leap year 
'''
def is_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter the year: "))
print(is_leap(year))