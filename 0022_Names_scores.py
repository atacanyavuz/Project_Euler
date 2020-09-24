"""


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
alphabet = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def name_score(name):
    score = 0
    for i in name:
        score += alphabet.index(i)
    return score

with open("p022_names.txt", "r+") as file:
    x = file.read().replace('"', " ").replace(",", " ")
    all_names = x.split()

total_score = 0
all_names.sort()
for i in range(len(all_names)):
    total_score = total_score + ((i + 1) * name_score(all_names[i]))

print(total_score)




