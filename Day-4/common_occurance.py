'''
Docstring for Day-4.common_occurance
Given a string which is the company name in lowercase letters your task is to find the 
top three  most common character in the string 
print the three most common character along with their occurance count
If the occurance count is the same, sort the characters in alphabetical order
'''


s = str(input("Entert the string: "))
#s = "sdfghjkertyuifghj"

freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

items = list(freq.items())
items.sort(key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(items[i][0], items[i][1])


