with open ("input3") as f:
    lines = f.read()
import string
import collections

lines = lines.split("\n")
alphabet = list(string.ascii_letters)

print(lines)

list_of_items = []
for line in lines:
    middle = int(len(line)/2)
    line1 = line[0:middle]
    line2 = line[middle:len(line)]
    #print(line1)
    #print(line2)
    i = 0
    found = False
    while i < len(line1):
        letter1 = line1[i]
        i += 1
        b = 0
        while b < len(line2) and found == False:
            letter2 = line2[b]
            b += 1
            if letter1 == letter2:
                list_of_items.append(letter1)
                found = True
sum_of_priorities = 0
for entry in list_of_items:
    sum_of_priorities += alphabet.index(entry)+1
print(sum_of_priorities)


line1 = lines[0]
line2 = lines[1]
line3 = lines[2]

i = 0
found = False
team_item = []
while i < len(lines)-2:
    for letter1 in lines[i]:
        for letter2 in lines[i+1]:
            for letter3 in lines[i+2]:
                if letter1 == letter2 and letter1 == letter3 and found == False:
                    team_item += letter1
                    found = True
    found = False
    i += 3

print(team_item)
print(len(team_item))

sum_of_priorities2 = 0
for entry in team_item:
    sum_of_priorities2 += alphabet.index(entry)+1
print(sum_of_priorities2)

