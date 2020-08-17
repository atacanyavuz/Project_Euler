"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

numeral = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ""]
first_twenty = ["ten", "elevan", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tenners = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def how_many_latter(x):
    if x < 10:
        return len(numeral[x-1])

    elif x < 20:
        return len(first_twenty[x-10])

    elif x < 100:
        return len(tenners[ x//10 - 2]) + len(numeral[(x%10) - 1])

    elif x % 100 == 0 and x < 1000:
        return len(numeral[(x // 100) - 1]) + 7

    elif x < 1000:
        return len(numeral[(x // 100) - 1]) + 10 + how_many_latter(x % 100)

    elif x == 1000:
        return 11

total = 0
for i in range(1, 1001):
    total = total + how_many_latter(i)

print(total)




