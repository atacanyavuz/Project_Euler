"""
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
"""

def next_month_first_day(first_day, month_day):
    x = month_day % 7
    return (first_day + x) % 7


total_sundays = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_day = 0   # 0 is Monday

# 1 Jan 1901
for i in month:
    first_day = next_month_first_day(first_day, i)

for j in range(1901, 2001):
    if j % 4 != 0:
        for i in month:
            first_day = next_month_first_day(first_day, i)
            if first_day == 6:
                total_sundays = total_sundays + 1
    else:
        for i in month:
            if i == 28:
                first_day = next_month_first_day(first_day, 29)
            else:
                first_day = next_month_first_day(first_day, i)
            if first_day == 6:
                total_sundays = total_sundays + 1

print(total_sundays)

