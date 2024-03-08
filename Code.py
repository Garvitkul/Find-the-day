#Defining leap year function
def isLeap(yr) :
    if yr%4 == 0 :
        if yr%100 == 0 :
            if yr%400 == 0 :
                return True
            else :
                return False
        return True
    else :
        return False
# Defining main function of the script that finds the day of any date

def findDay(date, month, year) :
    days = {
        0 : 'Sunday',
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wednesday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'Saturday',
        7 : 'Sunday'

    }

    mon = {
        1 : 6,
        2 : 2,
        3 : 2,
        4 : 5,
        5 : 7,
        6 : 3,
        7 : 5,
        8 : 1,
        9 : 4,
        10 : 6,
        11 : 2,
        12 : 4
    }
    if isLeap(year) :
        mon[1] = 5
        mon[2] = 1

    if ((year >= 900 and year <= 999) or (year >= 1300 and year <= 1399) or (year >= 1700 and year <= 1799) or (year >= 2100 and year <= 2199)) :
        formula = date + mon[month] + int(year%100) + int((year%100)/4) + 5
        day = days[formula%7]

    elif ((year >= 1000 and year <= 1099) or (year >= 1400 and year <= 1499) or (year >= 1800 and year <= 1899) or (year >= 2200 and year <= 2299)) :
        formula = date + mon[month] + int(year%100) + int((year%100)/4) + 3
        day = days[formula%7]

    elif ((year >= 1100 and year <= 1199) or (year >= 1500 and year <= 1599) or (year >= 1900 and year <= 1999) or (year >= 2300 and year <= 2399)) :
        formula = date + mon[month] + int(year%100) + int((year%100)/4) + 1
        day = days[formula%7]

    elif ((year >= 1200 and year <= 1299) or (year >= 1600 and year <= 1699) or (year >= 2000 and year <= 2099) or (year >= 2400 and year <= 2499)) :
        formula = date + mon[month] + int(year%100) + int((year%100)/4)
        day = days[formula%7]

    else :
        return "Please Enter Valid date/month/year.."
    
    return day

# Giving input to the function 
date = int(input("Enter Date : "))
month  = int(input("Enter Month : "))
year = int(input("Enter Year : "))

# Calling the function
findDay(date,month,year)
