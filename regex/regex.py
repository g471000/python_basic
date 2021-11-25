import re

filename = input("What is file name?")
if len(filename) == 0:
    filename = "regex_sum_1420324.txt"
handle = open(filename)

total = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for n in numbers:
        total = total + int(n)

print(total)
