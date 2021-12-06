'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
def is_leap_year(n):
    return n % 4 == 0 and n % 100 != 0


months = {'jan': 31, 'feb': 28, 'mar': 31, "apr": 30, "may": 31, "jun": 30, "jul": 31, "aug": 31, "sep": 30, "oct": 31, "nov": 30, "dec": 31}
months_arr = []
for i in months:
    months_arr.append(i)
year = 1901
date = 1
month = "jan"
day = 3
count = 0
while year != 2000 or month != "dec" or date != 31:
    if date == 1 and day == 1:
        count += 1
    day += 1
    if day > 7:
        day = 1
    date += 1
    if date > months[month]:
        date = 1
        if month == "dec":
            year += 1
            if is_leap_year(year):
                months['feb'] = 29
            else:
                months['feb'] = 28
            month = 'jan'
        else:
            month = months_arr[months_arr.index(month) + 1]
print(count)
